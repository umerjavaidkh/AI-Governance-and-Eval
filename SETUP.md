# 🚀 Setup Guide — AI Governance and Eval

This repo ships **already populated** (see `README.md`) plus an agent that keeps
it updated automatically. Here's how to get it live.

## 1. Push these files to your repo

From this folder:

```bash
git init
git add .
git commit -m "feat: seed AI Governance and Eval + auto-update agent"
git branch -M main
git remote add origin https://github.com/umerjavaidkh/AI-Governance-and-Eval.git
git push -u origin main
```

(If the remote already has commits, use `git pull --rebase origin main` first.)

## 2. Let the agent commit back to the repo

The scheduled workflow regenerates `README.md` and `data/collection.json` and
pushes the changes. For that push to succeed:

1. Go to **Settings → Actions → General**.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Save.

The workflow already requests `contents: write`, and the built-in `GITHUB_TOKEN`
is used automatically — no personal token or secret needed.

## 3. (Optional) Spotlight blurbs

The 🏆 Category Leaders section uses a human-written `best_for` line when the
entry has one, and only calls an LLM for entries that don't. To enable that,
add **`OPENAI_API_KEY`** (or `ANTHROPIC_API_KEY`, and set
`spotlights.provider: anthropic`) under **Settings → Secrets and variables →
Actions**. Without a key the agent skips spotlights silently.

## 4. (Optional) Run it now

You don't have to wait for the schedule:

- **Actions tab → “Update AI Governance and Eval” → Run workflow**, or
- locally:

  ```bash
  pip install -r requirements.txt
  GITHUB_TOKEN=<your_personal_token> python scripts/update_collection.py
  ```

  A token is optional locally but avoids GitHub's low anonymous rate limit
  (60 core requests/hour, 10 searches/minute).

### Smoke-test flags

Useful when you're tuning `config.yaml` and don't want to burn rate limit:

| Flag | Effect |
| ---- | ------ |
| `--skip-discovery` | curated entries only, zero Search API calls |
| `--skip-refresh` | don't refresh stars for curated repos |
| `--limit-topics N` | only scan the first N search topics |

## Schedule

Runs at **06:00 UTC every Monday** (`cron: "0 6 * * 1"` in
`.github/workflows/update-collection.yml`).

- For **every 2 days**, change the cron to `"0 6 */2 * *"`.
- For a specific hour, change the `6`.

## Tuning what gets collected

Everything lives in [`config.yaml`](config.yaml):

| Want to… | Do this |
| -------- | ------- |
| Change the discovery star threshold | edit `min_stars` |
| Add a topic to scan | add to `search_topics` |
| Add / rename a category | edit `categories` |
| Move a category leader to the top | set `rank:` on that entry in `data/curated.yaml` |
| Add or edit a compliance deadline | edit `deadlines` |
| Publish discoveries straight into the list | set `discovery_mode: inline` |
| Loosen or tighten discovery precision | edit `min_discovery_score` |
| Kick out a spam / novelty repo | add its `owner/name` to `blocklist` |
| Reject a whole class of repo | add a phrase to `reject_keywords` |

No Python changes are ever required for tuning.

## The one thing to maintain by hand

[`data/curated.yaml`](data/curated.yaml) is the reason this list is worth
reading. The agent never writes to it. Everything a regulator or auditor cares
about — the EU AI Act, NIST AI RMF, ISO/IEC 42001, OWASP, MITRE ATLAS — has no
GitHub repo and therefore no stars, so no amount of API scanning will discover
it. Adding one good entry there is worth more than a hundred discovered repos.
