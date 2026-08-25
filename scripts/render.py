"""README rendering for AI Governance and Eval.

Split out of the agent because presentation is now the bulk of the work. The
layout is tuned for a narrow, specific domain: fewer entries than a general
"famous AI repos" list, so each one can afford real estate, and the reader is
usually looking for one specific thing rather than browsing.

Three things drive the design:

  * A compliance deadline countdown at the top, recomputed every run. A static
    list is read once; a countdown gets checked.
  * Three-column category tables with metadata stacked under the entry name,
    instead of a six-column table that wraps into mush on a phone.
  * Provenance badges everywhere, because in this domain "who published this"
    matters more than "how many stars does it have".
"""

from __future__ import annotations

from datetime import date, datetime, timezone

TIER_CURATED, TIER_VERIFIED, TIER_FOUND = 1, 2, 3
TIER_BADGE = {TIER_CURATED: "🏛️", TIER_VERIFIED: "✅", TIER_FOUND: "🔎"}
TIER_WORD = {TIER_CURATED: "Authoritative", TIER_VERIFIED: "Verified", TIER_FOUND: "Candidate"}


def stars_str(n: int | None) -> str:
    if not n:
        return ""
    if n >= 1000:
        return f"⭐ {n / 1000:.1f}k".replace(".0k", "k")
    return f"⭐ {n}"


def _bar(value: int, total: int, width: int = 14) -> str:
    """Block-character bar. Renders identically everywhere, unlike an image."""
    if total <= 0:
        return "░" * width
    filled = max(1, round(width * value / total)) if value else 0
    return "█" * filled + "░" * (width - filled)


def _hook(entry: dict) -> str:
    """Human-written best_for beats a generated spotlight beats nothing."""
    return entry.get("best_for") or entry.get("spotlight") or ""


def _clean(text: str, limit: int) -> str:
    out = (text or "").replace("|", "\\|").replace("\n", " ").strip()
    return out[: limit - 3].rstrip() + "..." if len(out) > limit else out


def _entry_cell(entry: dict, is_new: bool) -> str:
    """Entry name plus stacked metadata — keeps the table to three columns."""
    badge = TIER_BADGE[entry["tier"]]
    name = f"{badge} **[{entry['name']}]({entry['url']})**"
    if is_new:
        name += " 🆕"
    if entry.get("archived"):
        name += " 🗄️"

    bits = []
    if entry.get("jurisdiction"):
        bits.append(f"`{entry['jurisdiction']}`")
    if entry.get("status"):
        bits.append(f"`{entry['status']}`")
    if entry.get("license"):
        bits.append(f"`{entry['license']}`")
    stars = stars_str(entry.get("stars"))
    if stars:
        bits.append(stars)

    meta = f"<br><sub>{entry['org']}{' · ' if bits else ''}{' '.join(bits)}</sub>"
    return name + meta


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #
def _hero(total: int, tiers: dict, cats: int, stamp: str, now: datetime) -> list[str]:
    return [
        '<div align="center">',
        "",
        "# 🏛️ AI Governance and Eval",
        "",
        "**The frameworks regulators, auditors and frontier labs actually use.**",
        "",
        "Standards, safety policies, eval harnesses and red-team tooling in one place —",
        "each with a plain answer to *what is this* and *when would I reach for it*.",
        "",
        f"![Entries](https://img.shields.io/badge/entries-{total}-1f6feb?style=flat-square) "
        f"![Authoritative](https://img.shields.io/badge/authoritative-{tiers[1]}-8957e5?style=flat-square) "
        f"![Verified tools](https://img.shields.io/badge/verified_tools-{tiers[2]}-2da44e?style=flat-square) "
        f"![Updated](https://img.shields.io/badge/updated-{now:%Y--%m--%d}-0969da?style=flat-square) "
        "![License](https://img.shields.io/badge/license-MIT-6e7781?style=flat-square)",
        "",
        f"`{total} entries` · `{cats} categories` · auto-updated every Monday · "
        f"last run {stamp}",
        "",
        "</div>",
        "",
        "---",
        "",
    ]


def _deadlines(config: dict) -> list[str]:
    """Countdown to real compliance dates. Recomputed on every run."""
    items = config.get("deadlines") or []
    if not items:
        return []

    today = date.today()
    rows, upcoming = [], 0
    for item in sorted(items, key=lambda d: d["date"]):
        when = date.fromisoformat(item["date"])
        days = (when - today).days

        if days < 0:
            if days < -365:
                continue  # older than a year: no longer useful context
            status = "✅ **In force**"
        elif days <= 90:
            status = f"🔴 **{days} days**"
            upcoming += 1
        elif days <= 365:
            status = f"🟠 **{days} days**"
            upcoming += 1
        else:
            status = f"🟢 {days} days"
            upcoming += 1

        label = f"[{item['label']}]({item['url']})" if item.get("url") else item["label"]
        rows.append(f"| `{item['date']}` | {status} | {label} | {item.get('scope', '')} |")

    if not rows:
        return []

    return [
        "## ⏱️ Compliance countdown",
        "",
        f"_{upcoming} deadline(s) still ahead. Recalculated every run — "
        "this is the number your programme plan is racing._",
        "",
        "| Date | Status | What applies | Instrument |",
        "| :--- | :----- | :----------- | :--------- |",
        *rows,
        "",
        "> ⚠️ **Not legal advice.** Dates move — the Digital Omnibus shifted the",
        "> high-risk tier in mid-2026. Verify against primary sources before",
        "> committing budget.",
        "",
        "---",
        "",
    ]


def _legend(tiers: dict, candidates_mode: bool) -> list[str]:
    lines = [
        "## 🎯 How to read this list",
        "",
        "Stars measure fame, not trustworthiness. Every entry carries a provenance",
        "badge, and **the list sorts on that badge before anything else** — so a",
        "60k-star wrapper can never outrank the EU AI Act.",
        "",
        "| | Tier | What it means | Count |",
        "| :-: | :--- | :------------ | ----: |",
        f"| 🏛️ | **Authoritative** | Published by a regulator, standards body or national "
        f"institute. No repo, no stars, and the reason most people are here. | **{tiers[1]}** |",
        f"| ✅ | **Verified** | Open-source tooling a human vetted and pinned in "
        f"[`data/curated.yaml`](data/curated.yaml). | **{tiers[2]}** |",
    ]
    if candidates_mode:
        lines.append(
            f"| 🔎 | **Candidate** | Surfaced by the agent, unreviewed, and deliberately kept "
            f"[out of the main list](#-candidates-for-review) until a human checks it. | "
            f"**{tiers[3]}** |"
        )
    else:
        lines.append(
            f"| 🔎 | **Discovered** | Found automatically, not yet reviewed. A lead, not a "
            f"recommendation. | **{tiers[3]}** |"
        )
    lines += ["", "---", ""]
    return lines


def _start_here(cat_meta: dict) -> list[str]:
    picks = [
        ("🇪🇺", "Ship into the EU market", "regulation", "EU AI Act + Digital Omnibus"),
        ("🧭", "Stand up governance from zero", "risk", "NIST AI RMF"),
        ("📋", "Pass enterprise procurement", "risk", "ISO/IEC 42001"),
        ("🛡️", "Threat-model a RAG or agent app", "security", "OWASP Top 10 for LLMs"),
        ("📏", "Benchmark a base model credibly", "harness", "lm-evaluation-harness"),
        ("🧪", "Run safety or agentic evals", "harness", "Inspect"),
        ("🔬", "Test *your* product, not the model", "appeval", "Ragas / DeepEval"),
        ("🐙", "Attack your own endpoint first", "redteam", "garak"),
    ]
    lines = [
        "## 🚦 Start here",
        "",
        "_Skip the browsing. Find your row, open the thing in the last column._",
        "",
        "| | I need to… | Open this first | Section |",
        "| :-: | :--------- | :-------------- | :------ |",
    ]
    for icon, need, slug, pick in picks:
        if slug in cat_meta:
            lines.append(f"| {icon} | {need} | **{pick}** | [{cat_meta[slug]['name']}](#cat-{slug}) |")
    lines += ["", "---", ""]
    return lines


def _leaders(non_empty: list[str], by_cat: dict, cat_meta: dict) -> list[str]:
    picks = [(cat_meta[s]["name"], by_cat[s][0]) for s in non_empty if _hook(by_cat[s][0])]
    if not picks:
        return []

    lines = [
        "## 🏆 One pick per category",
        "",
        "_If you read nothing else._",
        "",
    ]
    for cat_name, e in picks:
        stars = stars_str(e.get("stars"))
        tail = f" <sub>· {stars}</sub>" if stars else ""
        lines.append(f"**{cat_name}**  ")
        lines.append(f"{TIER_BADGE[e['tier']]} [{e['name']}]({e['url']}) — {_hook(e)}{tail}")
        lines.append("")
    lines += ["---", ""]
    return lines


def _momentum(entries: list[dict], config: dict, cat_meta: dict) -> list[str]:
    per_cat_cap = int(config.get("trending_per_category", 3))
    movers = [
        e for e in entries
        if e.get("prev_stars") and e.get("stars") and e["stars"] > e["prev_stars"]
    ]
    movers.sort(key=lambda e: e["stars"] - e["prev_stars"], reverse=True)

    picked, per_cat = [], {}
    for e in movers:
        slug = e["category_slug"]
        if per_cat.get(slug, 0) >= per_cat_cap:
            continue
        per_cat[slug] = per_cat.get(slug, 0) + 1
        picked.append(e)
        if len(picked) >= int(config.get("trending_count", 8)):
            break

    if not picked:
        return []

    lines = [
        "## 📈 Momentum",
        "",
        "_Fastest-growing tools since the last run, capped per category so one hot "
        "bucket can't fill the table._",
        "",
        "| Project | Stars | Gain | Category |",
        "| :------ | ----: | ---: | :------- |",
    ]
    for e in picked:
        gain = e["stars"] - e["prev_stars"]
        gain_s = f"+{gain / 1000:.1f}k".replace(".0k", "k") if gain >= 1000 else f"+{gain}"
        cat = cat_meta[e["category_slug"]]["name"]
        lines.append(
            f"| **[{e['name']}]({e['url']})** | {stars_str(e['stars'])} | 📈 {gain_s} | {cat} |"
        )
    lines += ["", "---", ""]
    return lines


def _contents(non_empty: list[str], by_cat: dict, cat_meta: dict) -> list[str]:
    lines = ["## 📑 Contents", "", "| Section | Entries | | Section | Entries |",
             "| :------ | ------: | :-: | :------ | ------: |"]
    half = (len(non_empty) + 1) // 2
    left, right = non_empty[:half], non_empty[half:]
    for i in range(half):
        lcell = f"[{cat_meta[left[i]]['name']}](#cat-{left[i]}) | {len(by_cat[left[i]])}"
        if i < len(right):
            rcell = f"[{cat_meta[right[i]]['name']}](#cat-{right[i]}) | {len(by_cat[right[i]])}"
        else:
            rcell = " | "
        lines.append(f"| {lcell} |  | {rcell} |")
    lines += ["", "---", ""]
    return lines


def _categories(non_empty: list[str], by_cat: dict, cat_meta: dict,
                new_ids: set[str], max_per_cat: int) -> list[str]:
    lines: list[str] = []
    for slug in non_empty:
        meta, items = cat_meta[slug], by_cat[slug]
        counts = [sum(1 for e in items if e["tier"] == t) for t in (1, 2)]

        lines.append(f'<a id="cat-{slug}"></a>')
        lines.append("")
        lines.append(f"## {meta['name']}")
        lines.append("")
        if meta.get("blurb"):
            lines.append(f"> {meta['blurb']}")
            lines.append("")
        lines.append(
            f"<sub>{len(items)} entries · {counts[0]} authoritative 🏛️ · "
            f"{counts[1]} verified ✅</sub>"
        )
        lines.append("")
        lines.append("| Entry | What it is | Reach for it when |")
        lines.append("| :---- | :--------- | :---------------- |")
        for e in items[:max_per_cat]:
            lines.append(
                f"| {_entry_cell(e, e['id'] in new_ids)} | {_clean(e.get('description', ''), 330)} "
                f"| {_hook(e) or '—'} |"
            )
        remaining = len(items) - max_per_cat
        if remaining > 0:
            lines.append(
                f"| _+{remaining} more in [`data/collection.json`](data/collection.json)_ | | |"
            )
        lines.append("")
        lines.append('<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>')
        lines.append("")
    lines += ["---", ""]
    return lines


def _candidates(candidates: list[dict], cat_meta: dict) -> list[str]:
    if not candidates:
        return []
    lines = [
        "## 🔎 Candidates for review",
        "",
        f"**{len(candidates)} projects** the agent found on the configured GitHub topics "
        "that **no human has vetted**. They sit here rather than in the categories above "
        "because a GitHub topic is self-declared — anyone shipping an agent product can "
        "tag it `ai-safety`. Treat these as leads to investigate, not recommendations.",
        "",
        "> 💡 **Used one of these in anger?** That's the most valuable PR you can open: "
        "move it into [`data/curated.yaml`](data/curated.yaml) with a `best_for` line and "
        "today's date, and it joins the real list.",
        "",
        "<details>",
        f"<summary><b>Show {len(candidates)} unreviewed candidates</b></summary>",
        "",
        "| Project | Stars | Suggested category | Description |",
        "| :------ | ----: | :----------------- | :---------- |",
    ]
    for e in candidates[:50]:
        cat = cat_meta.get(e["category_slug"], {}).get("name", "—")
        lines.append(
            f"| [{e['name']}]({e['url']}) | {stars_str(e.get('stars')) or '—'} | {cat} "
            f"| {_clean(e.get('description', ''), 110)} |"
        )
    lines += ["", "</details>", "", "---", ""]
    return lines


def _stats(non_empty: list[str], by_cat: dict, cat_meta: dict, tiers: dict, total: int) -> list[str]:
    peak = max((len(by_cat[s]) for s in non_empty), default=1)
    lines = [
        "## 📊 Coverage",
        "",
        "| Section | | 🏛️ | ✅ | Total |",
        "| :------ | :-- | -: | -: | ----: |",
    ]
    for slug in non_empty:
        items = by_cat[slug]
        counts = [sum(1 for e in items if e["tier"] == t) for t in (1, 2)]
        lines.append(
            f"| {cat_meta[slug]['name']} | `{_bar(len(items), peak)}` | {counts[0]} "
            f"| {counts[1]} | **{len(items)}** |"
        )
    lines.append(f"| **Total** | | **{tiers[1]}** | **{tiers[2]}** | **{total}** |")
    lines += ["", "---", ""]
    return lines


def _footer(config: dict) -> list[str]:
    return [
        "## 🤖 How this stays current",
        "",
        "```",
        "  data/curated.yaml  ──┐",
        "   (human-owned)       ├──►  update_collection.py  ──►  README.md",
        "  GitHub Search API  ──┘         (every Monday)          collection.json",
        "```",
        "",
        "1. A scheduled [GitHub Action](.github/workflows/update-collection.yml) runs the "
        "agent every Monday at 06:00 UTC.",
        "2. Authoritative frameworks and vetted tools are read from "
        "[`data/curated.yaml`](data/curated.yaml). **The agent never writes to that file** "
        "and never removes an entry from it.",
        "3. It then scans the GitHub Search API for the topics in "
        f"[`config.yaml`](config.yaml), keeping repos above **{config['min_stars']:,} stars** "
        "that pass the quality gate, and scores each into its best-fitting category.",
        "4. Discoveries land in [Candidates for review](#-candidates-for-review); they only "
        "join the main list when a human promotes them. Deadlines are recalculated, the "
        "README is regenerated, and changes are committed back.",
        "",
        "**Tuning takes no code.** `config.yaml` controls the star threshold, search topics, "
        "categories, quality gate, blocklist and deadlines. See [SETUP.md](SETUP.md).",
        "",
        "## 🙌 Contributing",
        "",
        "| Contribution | Why it matters |",
        "| :----------- | :------------- |",
        "| **Promote a 🔎 candidate to ✅** | The highest-value PR here. If you've used the "
        "tool for real, add it to `data/curated.yaml` with a `best_for` line. |",
        "| **Fix a moved deadline or status** | Cite the primary source and it merges fast. |",
        "| **Add a non-EU/US/UK/SG framework** | Coverage is thinnest outside those "
        "jurisdictions. |",
        "| **Report a mis-sorted entry** | The categoriser scores topics; a bad score is a "
        "config fix. |",
        "",
        "A good `best_for` line is specific. *\"Evaluating LLMs\"* gets rejected; *\"Proving a "
        "RAG answer is grounded in retrieved context\"* gets merged.",
        "",
        "<div align=\"center\">",
        "",
        "**Found this useful? A ⭐ keeps it maintained and helps the next person find it.**",
        "",
        "Released under the [MIT License](LICENSE). "
        "Framework and repository metadata belongs to its respective owners.",
        "",
        "</div>",
        "",
    ]


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
def render_readme(store: dict, config: dict, new_ids: set[str], group_by_category) -> str:
    cat_meta = {c["slug"]: c for c in config["categories"] + [config["fallback_category"]]}
    all_entries = list(store["entries"].values())

    candidates_mode = config.get("discovery_mode", "candidates") == "candidates"
    if candidates_mode:
        entries = [e for e in all_entries if e["tier"] != TIER_FOUND]
        candidates = sorted(
            (e for e in all_entries if e["tier"] == TIER_FOUND),
            key=lambda e: -(e.get("stars") or 0),
        )
    else:
        entries, candidates = all_entries, []

    cat_order, by_cat = group_by_category(entries, config)
    non_empty = [s for s in cat_order if by_cat.get(s)]
    total = len(entries)
    tiers = {t: sum(1 for e in all_entries if e["tier"] == t) for t in (1, 2, 3)}
    now = datetime.now(timezone.utc)

    out: list[str] = []
    out += _hero(total, tiers, len(non_empty), now.strftime("%Y-%m-%d %H:%M UTC"), now)
    out += _deadlines(config)
    out += _start_here(cat_meta)
    out += _legend(tiers, candidates_mode)
    out += _leaders(non_empty, by_cat, cat_meta)
    out += _momentum(entries, config, cat_meta)
    out += _contents(non_empty, by_cat, cat_meta)
    out += _categories(non_empty, by_cat, cat_meta, new_ids,
                       int(config.get("max_per_category", 15)))
    out += _candidates(candidates, cat_meta)
    out += _stats(non_empty, by_cat, cat_meta, tiers, total)
    out += _footer(config)

    return "\n".join(out)
