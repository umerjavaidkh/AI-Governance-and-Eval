#!/usr/bin/env python3
"""
AI Governance and Eval — auto-update agent.

Merges three intake tiers into one list, then regenerates README.md:

  tier 1 (curated)  authoritative frameworks from data/curated.yaml that have
                    no GitHub presence — EU AI Act, NIST AI RMF, ISO/IEC 42001,
                    OWASP, MITRE ATLAS. Star-based discovery cannot find these.
  tier 2 (verified) open-source tools pinned in data/curated.yaml with a repo,
                    whose stars the agent refreshes but which it never drops.
  tier 3 (found)    discovered from the GitHub Search API and labelled 🔎 until
                    a human promotes them into curated.yaml.

State lives in data/collection.json (first_seen, prev_stars, spotlight cache).

Designed to run on a schedule via GitHub Actions, but also runnable locally:

    GITHUB_TOKEN=<your token> python scripts/update_collection.py

An unauthenticated run works too but is heavily rate-limited by GitHub.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import render_readme  # noqa: E402  (needs the path insert above)

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.yaml"
CURATED_PATH = ROOT / "data" / "curated.yaml"
DATA_PATH = ROOT / "data" / "collection.json"
README_PATH = ROOT / "README.md"

SEARCH_API = "https://api.github.com/search/repositories"
REPO_API = "https://api.github.com/repos"
ANTHROPIC_API = "https://api.anthropic.com/v1/messages"
OPENAI_API = "https://api.openai.com/v1/chat/completions"
SESSION = requests.Session()

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

TIER_CURATED, TIER_VERIFIED, TIER_FOUND = 1, 2, 3
TIER_BADGE = {TIER_CURATED: "🏛️", TIER_VERIFIED: "✅", TIER_FOUND: "🔎"}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc):%H:%M:%S}] {msg}", flush=True)


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_curated() -> dict:
    with open(CURATED_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_existing() -> dict:
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as fh:
            return json.load(fh)
    return {"entries": {}}


def stars_str(n: int | None) -> str:
    if not n:
        return "—"
    if n >= 1000:
        return f"⭐ {n / 1000:.1f}k".replace(".0k", "k")
    return f"⭐ {n}"


# --------------------------------------------------------------------------- #
# GitHub
# --------------------------------------------------------------------------- #
def _get(url: str) -> dict | None:
    """GET with backoff on rate limits. Returns None on permanent failure."""
    for attempt in range(4):
        resp = SESSION.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (403, 429):
            reset = resp.headers.get("X-RateLimit-Reset")
            wait = 5 * (attempt + 1)
            if reset:
                wait = max(wait, int(reset) - int(time.time()) + 2)
            wait = min(wait, 90)
            log(f"  rate-limited; sleeping {wait}s")
            time.sleep(wait)
            continue
        log(f"  {url.split('/')[-1]} -> HTTP {resp.status_code}; skipping")
        return None
    return None


def fetch_topic(topic: str, min_stars: int, pages: int) -> list[dict]:
    """Fetch repos for a single GitHub topic, paginating politely."""
    out: list[dict] = []
    query = quote(f"topic:{topic} stars:>{min_stars}", safe=":>")
    for page in range(1, pages + 1):
        payload = _get(f"{SEARCH_API}?q={query}&sort=stars&order=desc&per_page=100&page={page}")
        if payload is None:
            return out
        items = payload.get("items", [])
        out.extend(items)
        if len(items) < 100:
            break
        time.sleep(1)  # be gentle with the search API
    return out


def fetch_repo(full_name: str) -> dict | None:
    return _get(f"{REPO_API}/{full_name}")


# --------------------------------------------------------------------------- #
# Filtering and categorisation
# --------------------------------------------------------------------------- #
def passes_quality(repo: dict, quality: dict, blocklist: set[str], reject: list[str]) -> bool:
    if repo["full_name"].lower() in blocklist:
        return False
    if quality.get("exclude_forks", True) and repo.get("fork"):
        return False
    if quality.get("exclude_archived", True) and repo.get("archived"):
        return False
    if quality.get("exclude_disabled", True) and repo.get("disabled"):
        return False

    desc = (repo.get("description") or "").strip()
    if quality.get("require_description", True) and not desc:
        return False

    haystack = f"{repo.get('name', '')} {desc}".lower()
    if any(bad.lower() in haystack for bad in reject):
        return False

    months = quality.get("max_months_since_push")
    if months and repo.get("pushed_at"):
        pushed = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
        if pushed < datetime.now(timezone.utc) - timedelta(days=30 * int(months)):
            return False

    return True


def categorize(repo: dict, categories: list[dict], fallback: dict) -> tuple[str, str, int]:
    """Return (category_name, category_slug, score) for the BEST-scoring category.

    First-match-wins is wrong here because a repo's topic set is unordered and
    frequently spans several categories. huggingface/transformers, for example,
    carries `speech-recognition` alongside `nlp` — under first-match-wins, any
    Speech category listed above LLMs captures it and stops looking, which is
    how a foundation-model library ends up leading a speech section.

    Scoring: an explicit maintainer-set topic is worth 3, a keyword hit on the
    name/description is worth 1. Ties break by config order, so specific
    categories should still be listed first.
    """
    topics = {t.lower() for t in (repo.get("topics") or [])}
    haystack = f"{repo.get('name', '')} {repo.get('description', '')}".lower()

    best_score, best = 0, None
    for cat in categories:
        score = 3 * len(topics & {t.lower() for t in cat.get("topics", [])})
        score += sum(1 for kw in cat.get("keywords", []) if kw.lower() in haystack)
        if score > best_score:
            best_score, best = score, cat

    if best is None:
        return fallback["name"], fallback["slug"], 0
    return best["name"], best["slug"], best_score


# --------------------------------------------------------------------------- #
# Intake
# --------------------------------------------------------------------------- #
def curated_entries(curated: dict, config: dict) -> dict[str, dict]:
    """Verified repos from data/curated.yaml, keyed by entry id."""
    cat_slugs = {c["slug"] for c in config["categories"]} | {config["fallback_category"]["slug"]}
    out: dict[str, dict] = {}

    for raw in curated.get("entries", []):
        # Repos only, by design. A paper, article, regulation or framework has no
        # repo and is rejected here rather than silently rendered as an entry.
        if not raw.get("repo"):
            log(f"  curated '{raw['id']}': no repo, skipped (this list is repos only)")
            continue
        slug = raw.get("category")
        if slug not in cat_slugs:
            log(f"  curated '{raw['id']}': unknown category {slug!r}, using fallback")
            slug = config["fallback_category"]["slug"]

        out[raw["id"]] = {
            "id": raw["id"],
            "name": raw["name"],
            "org": raw["org"],
            "url": raw["url"],
            "description": raw["summary"],
            "best_for": raw.get("best_for", ""),
            "status": raw.get("status"),
            "license": raw.get("license"),
            "verified": raw.get("verified"),
            "rank": int(raw.get("rank", 100)),
            "full_name": raw.get("repo"),
            "category_slug": slug,
            "tier": TIER_VERIFIED,
            "stars": None,
            "topics": [],
        }
    return out


def discovered_entries(config: dict, limit_topics: int | None = None) -> dict[str, dict]:
    """Tier 3 from the GitHub Search API."""
    quality = config.get("quality", {})
    blocklist = {b.lower() for b in (config.get("blocklist") or [])}
    reject = config.get("reject_keywords") or []
    cats, fallback = config["categories"], config["fallback_category"]
    min_score = int(config.get("min_discovery_score", 3))
    skipped_score = 0

    topics = config["search_topics"]
    if limit_topics:
        topics = topics[:limit_topics]
        log(f"  limiting discovery to {len(topics)} topic(s)")

    seen: dict[str, dict] = {}
    for topic in topics:
        repos = fetch_topic(topic, int(config["min_stars"]), int(config["pages_per_topic"]))
        kept = 0
        for repo in repos:
            if repo["full_name"] in seen:
                continue
            if not passes_quality(repo, quality, blocklist, reject):
                continue
            name, slug, score = categorize(repo, cats, fallback)
            if score < min_score:
                # Keyword-only matches are noise on these topics: GitHub's
                # `ai-governance` and `ai-safety` tags attract anything that
                # mentions agents. Requiring an explicit maintainer-set topic
                # (worth 3) is the cheapest precision win available.
                skipped_score += 1
                continue
            seen[repo["full_name"]] = {
                "id": repo["full_name"],
                "name": repo["full_name"],
                "org": repo["owner"]["login"],
                "url": repo["html_url"],
                "description": (repo.get("description") or "").strip(),
                "best_for": "",
                "full_name": repo["full_name"],
                "category_slug": slug,
                "tier": TIER_FOUND,
                "rank": 100,
                "stars": repo.get("stargazers_count"),
                "license": (repo.get("license") or {}).get("spdx_id"),
                "topics": repo.get("topics") or [],
            }
            kept += 1
        log(f"  topic:{topic} -> {len(repos)} fetched, {kept} new kept")
    if skipped_score:
        log(f"  {skipped_score} rejected: no explicit topic match (score < {min_score})")
    return seen


def refresh_curated_repos(entries: dict[str, dict]) -> None:
    """Fill in stars for tier-2 entries and flag any repo that went archived."""
    for entry in entries.values():
        if entry["tier"] != TIER_VERIFIED or not entry.get("full_name"):
            continue
        repo = fetch_repo(entry["full_name"])
        if repo is None:
            continue  # fail soft: keep whatever we had
        entry["stars"] = repo.get("stargazers_count")
        entry["topics"] = repo.get("topics") or []
        if repo.get("archived"):
            entry["archived"] = True
            log(f"  ARCHIVED: {entry['full_name']} needs human review")


# --------------------------------------------------------------------------- #
# Merge
# --------------------------------------------------------------------------- #
def merge(store: dict, fresh: dict[str, dict]) -> tuple[dict, set[str]]:
    """Merge into the store, tracking first_seen and prev_stars."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    old = store.get("entries", {})
    merged: dict[str, dict] = {}
    new_ids: set[str] = set()

    for key, entry in fresh.items():
        prior = old.get(key)
        if prior is None:
            entry["first_seen"] = today
            new_ids.add(key)
        else:
            entry["first_seen"] = prior.get("first_seen", today)
            entry["prev_stars"] = prior.get("stars")
            # Spotlights are expensive; reuse unless the entry changed leader.
            if prior.get("spotlight"):
                entry["spotlight"] = prior["spotlight"]
        merged[key] = entry

    dropped = set(old) - set(merged)
    if dropped:
        log(f"  {len(dropped)} entries fell out of range this run")

    return {"entries": merged, "updated": today}, new_ids


def group_by_category(entries: list[dict], config: dict) -> tuple[list[str], dict[str, list[dict]]]:
    """Bucket into config category order, sorted by tier then stars desc.

    Tier leads the sort deliberately: a 60k-star wrapper must never outrank the
    EU AI Act in a governance list. Fame is the tie-breaker, not the ranking.
    """
    cats = config["categories"] + [config["fallback_category"]]
    cat_order = [c["slug"] for c in cats]
    # tier, then explicit rank, then stars. Authoritative entries have no stars
    # at all, so without `rank` a category leader would just be whichever
    # standards body comes first alphabetically.
    ordered = sorted(
        entries,
        key=lambda e: (e["tier"], e.get("rank", 100), -(e.get("stars") or 0), e["name"].lower()),
    )
    by_cat: dict[str, list[dict]] = {slug: [] for slug in cat_order}
    for entry in ordered:
        by_cat.setdefault(entry["category_slug"], []).append(entry)
    return cat_order, by_cat


# --------------------------------------------------------------------------- #
# Spotlights
# --------------------------------------------------------------------------- #
def _spotlight_prompt(entry: dict) -> str:
    return (
        "In one punchy sentence (under 22 words), tell a senior AI governance or "
        "ML engineer why this is worth their time — be specific and concrete, no "
        "generic marketing language. No preamble, just the sentence.\n\n"
        f"Name: {entry['name']}\n"
        f"Published by: {entry['org']}\n"
        f"Description: {entry.get('description', '')}\n"
        f"Topics: {', '.join(entry.get('topics', [])[:8])}"
    )


def _anthropic_spotlight(entry: dict, model: str, api_key: str) -> str | None:
    try:
        resp = SESSION.post(
            ANTHROPIC_API,
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": 100,
                "messages": [{"role": "user", "content": _spotlight_prompt(entry)}],
            },
            timeout=30,
        )
        resp.raise_for_status()
        blocks = resp.json().get("content", [])
        text = "".join(b.get("text", "") for b in blocks if b.get("type") == "text")
        return " ".join(text.split()) or None
    except (requests.RequestException, ValueError, KeyError) as exc:
        log(f"  spotlight for {entry['name']}: skipped ({type(exc).__name__})")
        return None


def _openai_spotlight(entry: dict, model: str, api_key: str) -> str | None:
    base = os.environ.get("OPENAI_BASE_URL", "").rstrip("/")
    url = f"{base}/chat/completions" if base else OPENAI_API
    try:
        resp = SESSION.post(
            url,
            headers={"Authorization": f"Bearer {api_key}", "content-type": "application/json"},
            json={
                "model": model,
                "max_tokens": 100,
                "messages": [{"role": "user", "content": _spotlight_prompt(entry)}],
            },
            timeout=30,
        )
        resp.raise_for_status()
        choices = resp.json().get("choices", [])
        text = choices[0]["message"]["content"] if choices else ""
        return " ".join(text.split()) or None
    except (requests.RequestException, ValueError, KeyError, IndexError) as exc:
        log(f"  spotlight for {entry['name']}: skipped ({type(exc).__name__})")
        return None


SPOTLIGHT_PROVIDERS = {
    "anthropic": {"fn": _anthropic_spotlight, "env_key": "ANTHROPIC_API_KEY",
                  "default_model": "claude-haiku-4-5-20251001"},
    "openai": {"fn": _openai_spotlight, "env_key": "OPENAI_API_KEY",
               "default_model": "gpt-4o-mini"},
}


def generate_spotlights(merged: dict[str, dict], by_cat: dict[str, list[dict]], config: dict) -> None:
    """Fill in entry['spotlight'] for each category's leader, in place."""
    scfg = config.get("spotlights", {})
    if not scfg.get("enabled", False):
        return
    provider = SPOTLIGHT_PROVIDERS.get(scfg.get("provider", "openai"))
    if provider is None:
        log(f"  spotlights: unknown provider {scfg.get('provider')!r}, skipping")
        return
    api_key = os.environ.get(provider["env_key"])
    if not api_key:
        log(f"  spotlights: {provider['env_key']} not set, skipping")
        return

    model = scfg.get("model") or provider["default_model"]
    made = 0
    for items in by_cat.values():
        if not items:
            continue
        leader = merged[items[0]["id"]]
        if leader.get("spotlight") or leader.get("best_for"):
            continue  # curated entries already carry a human-written hook
        why = provider["fn"](leader, model, api_key)
        if why:
            leader["spotlight"] = why
            made += 1
        time.sleep(0.3)
    log(f"  spotlights: generated {made} new blurb(s)")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-discovery", action="store_true",
                        help="curated entries only; no GitHub Search calls")
    parser.add_argument("--skip-refresh", action="store_true",
                        help="do not refresh stars for curated repos")
    parser.add_argument("--limit-topics", type=int, default=None,
                        help="only scan the first N search topics (smoke test)")
    args = parser.parse_args()

    log("loading config")
    config = load_config()
    curated = load_curated()

    log("reading curated entries")
    fresh = curated_entries(curated, config)
    log(f"  {len(fresh)} curated entries")

    if args.skip_refresh:
        log("skipping curated star refresh")
    else:
        log("refreshing curated repo stars")
        refresh_curated_repos(fresh)

    found: dict[str, dict] = {}
    if args.skip_discovery:
        log("skipping discovery")
    else:
        log("discovering repos")
        found = discovered_entries(config, args.limit_topics)
    # Curated wins on conflict: a human-written entry is never overwritten by
    # the discovery pass, even when the same repo turns up in both.
    pinned = {e["full_name"] for e in fresh.values() if e.get("full_name")}
    added = 0
    for key, entry in found.items():
        if key in pinned:
            continue
        fresh[key] = entry
        added += 1
    log(f"  {added} discovered entries added ({len(found) - added} already curated)")

    log("merging with history")
    store = load_existing()

    if args.skip_discovery:
        # Carry forward the existing candidate queue. Without this a smoke-test
        # run would quietly delete every discovery made so far, which is the
        # same class of bug as a failed refresh blanking good data.
        carried = 0
        for key, entry in store.get("entries", {}).items():
            if entry.get("tier") == TIER_FOUND and key not in fresh:
                fresh[key] = entry
                carried += 1
        if carried:
            log(f"  carried forward {carried} existing candidate(s)")

    store, new_ids = merge(store, fresh)

    _, by_cat = group_by_category(list(store["entries"].values()), config)
    log("generating spotlights")
    generate_spotlights(store["entries"], by_cat, config)

    log("writing data + README")
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as fh:
        json.dump(store, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write("\n")

    README_PATH.write_text(
        render_readme(store, config, new_ids, group_by_category), encoding="utf-8"
    )

    log(f"done — {len(store['entries'])} entries, {len(new_ids)} new")
    return 0


if __name__ == "__main__":
    sys.exit(main())
