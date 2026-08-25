<div align="center">

# 🏛️ AI Governance and Eval

**Open-source repos for evaluating AI and for governing it. Nothing else.**

Two domains: harnesses and suites that measure LLMs, agents and RAG pipelines,
and the platforms that run an AI governance programme. Every entry is a repo you
can clone — no papers, no articles, no regulations.

![Entries](https://img.shields.io/badge/entries-28-1f6feb?style=flat-square) ![Verified](https://img.shields.io/badge/verified-28-2da44e?style=flat-square) ![Updated](https://img.shields.io/badge/updated-2026--08--25-0969da?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-6e7781?style=flat-square)

`28 repos` · `2 domains` · auto-updated every Monday · last run 2026-08-25 05:27 UTC

</div>

---

## 🚦 Start here

_Skip the browsing. Find your row, open the thing in the last column._

| | I need to… | Open this first | Section |
| :-: | :--------- | :-------------- | :------ |
| 📏 | Benchmark a base model credibly | **lm-evaluation-harness** | [🧪 LLM, Agent & RAG Evaluation](#cat-eval) |
| 🧪 | Run safety or agentic evals | **Inspect** | [🧪 LLM, Agent & RAG Evaluation](#cat-eval) |
| 🔬 | Evaluate a RAG pipeline | **Ragas / DeepEval** | [🧪 LLM, Agent & RAG Evaluation](#cat-eval) |
| 🐙 | Attack your own endpoint first | **garak / PyRIT** | [🧪 LLM, Agent & RAG Evaluation](#cat-eval) |
| ⚖️ | Measure and mitigate bias | **Fairlearn / AIF360** | [🏛️ AI Governance Platforms](#cat-governance) |
| 🔍 | Explain a model decision | **InterpretML / Captum** | [🏛️ AI Governance Platforms](#cat-governance) |
| 📡 | Catch drift in production | **Evidently / Alibi Detect** | [🏛️ AI Governance Platforms](#cat-governance) |
| 🔐 | Keep PII out of prompts and logs | **Presidio** | [🏛️ AI Governance Platforms](#cat-governance) |

---

## 🎯 How to read this list

Stars measure fame, not trustworthiness. Every entry carries a provenance
badge, and **the list sorts on that badge before anything else** — so a
60k-star wrapper can never outrank a repo a human actually vetted.

| | Tier | What it means | Count |
| :-: | :--- | :------------ | ----: |
| ✅ | **Verified** | Open-source tooling a human vetted and pinned in [`data/curated.yaml`](data/curated.yaml). | **28** |
| 🔎 | **Candidate** | Surfaced by the agent, unreviewed, and deliberately kept [out of the main list](#-candidates-for-review) until a human checks it. | **0** |

---

## 🏆 One pick per category

_If you read nothing else._

**🧪 LLM, Agent & RAG Evaluation**  
✅ [DeepEval](https://github.com/confident-ai/deepeval) — Regression-testing an LLM feature in an existing Python CI pipeline.

**🏛️ AI Governance Platforms**  
✅ [AI Fairness 360](https://github.com/Trusted-AI/AIF360) — A broad menu of bias metrics when you don't yet know which one applies.

---

## 📑 Contents

| Section | Entries | | Section | Entries |
| :------ | ------: | :-: | :------ | ------: |
| [🧪 LLM, Agent & RAG Evaluation](#cat-eval) | 17 |  | [🏛️ AI Governance Platforms](#cat-governance) | 11 |

---

<a id="cat-eval"></a>

## 🧪 LLM, Agent & RAG Evaluation

> Repos you point at a model, an agent or a RAG pipeline to measure whether it actually works — harnesses, benchmarks, RAG/app eval, and adversarial testing.

<sub>17 repos · 17 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| ✅ **[DeepEval](https://github.com/confident-ai/deepeval)**<br><sub>Confident AI · `Actively maintained` `Apache-2.0`</sub> | Pytest-style evaluation for LLM apps — G-Eval, hallucination, task completion and custom metrics that fail a CI build like any other test. | Regression-testing an LLM feature in an existing Python CI pipeline. |
| ✅ **[garak](https://github.com/NVIDIA/garak)**<br><sub>NVIDIA · `Actively maintained` `Apache-2.0`</sub> | An LLM vulnerability scanner in the nmap tradition — dozens of probes for jailbreaks, prompt injection, data leakage, toxicity and encoding attacks. | A first automated red-team pass on any endpoint, in one command. |
| ✅ **[Giskard](https://github.com/Giskard-AI/giskard)**<br><sub>Giskard AI · `Actively maintained` `Apache-2.0`</sub> | Automated vulnerability scanning for ML and LLM apps — hallucination, bias, prompt injection, harmfulness — with reports oriented to EU AI Act evidence. | Generating compliance-shaped evidence from an automated scan. |
| ✅ **[HELM (Holistic Evaluation of Language Models)](https://crfm.stanford.edu/helm/)**<br><sub>Stanford CRFM · `Actively maintained` `Apache-2.0`</sub> | Multi-metric evaluation by design — accuracy, calibration, robustness, bias, toxicity, efficiency — with public leaderboards across domain variants. | Arguing that a single accuracy score is not an evaluation. |
| ✅ **[Inspect](https://inspect.aisi.org.uk/)**<br><sub>UK AI Security Institute · `Actively maintained` `MIT`</sub> | The evaluation framework a national safety institute uses on frontier models — solvers, scorers, tool use, multi-turn agents and human-in-the-loop, with a proper log viewer. | Safety and agentic evals you need to defend to an auditor. |
| ✅ **[Langfuse](https://github.com/langfuse/langfuse)**<br><sub>Langfuse · `Actively maintained` `MIT (core)`</sub> | Open-source LLM observability with datasets, scores, prompt management and human annotation queues; framework-agnostic. | Self-hosted production tracing with an evaluation loop attached. |
| ✅ **[LightEval](https://github.com/huggingface/lighteval)**<br><sub>Hugging Face · `Actively maintained` `MIT`</sub> | Lightweight, backend-agnostic evaluation pipeline used in leaderboard-style runs; easy to point at vLLM, TGI or an inference endpoint. | Fast iteration when a full harness is too heavy. |
| ✅ **[LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)**<br><sub>EleutherAI · `Actively maintained` `MIT`</sub> | The de facto standard for reproducible academic benchmarking; hundreds of tasks behind one interface, and the harness most published numbers come from. | Reporting MMLU/HellaSwag-class numbers others can reproduce. |
| ✅ **[METR Task Standard](https://github.com/METR/task-standard)**<br><sub>METR · `Stable, low activity` `MIT`</sub> | A specification for defining autonomous-capability tasks portably, so dangerous-capability evaluations can be shared and re-run across organisations. | Writing agent tasks that another lab can execute unchanged. |
| ✅ **[OpenCompass](https://github.com/open-compass/opencompass)**<br><sub>Shanghai AI Laboratory · `Actively maintained` `Apache-2.0`</sub> | Large bilingual (EN/CN) benchmark platform with broad dataset and model coverage, including domain suites for finance, healthcare and law. | Non-English and domain-specific coverage the Western harnesses miss. |
| ✅ **[Phoenix](https://github.com/Arize-ai/phoenix)**<br><sub>Arize AI · `Actively maintained` `Elastic-2.0`</sub> | Self-hostable, OpenTelemetry-native tracing and evaluation — traces become datasets, datasets become evals. | Observability and eval in one place, on your own infrastructure. |
| ✅ **[promptfoo](https://github.com/promptfoo/promptfoo)**<br><sub>promptfoo · `Actively maintained` `MIT`</sub> | Declarative YAML matrix testing across prompts, providers and assertions, with a strong adversarial/red-team generator. Note - reported in 2026 to be acquired by OpenAI; still MIT-licensed, but weigh vendor neutrality. | A/B testing a prompt or provider change without writing a harness. |
| ✅ **[Purple Llama / CyberSecEval](https://github.com/meta-llama/PurpleLlama)**<br><sub>Meta · `Active` `Custom`</sub> | Cybersecurity safety evaluations plus input/output guard models (Llama Guard, Code Shield) for insecure-code and attack-compliance testing. | Measuring whether a coding assistant emits insecure code. |
| ✅ **[PyRIT](https://github.com/microsoft/PyRIT)**<br><sub>Microsoft · `Actively maintained` `MIT`</sub> | Python Risk Identification Toolkit — orchestrators, converters and scorers for automating multi-turn adversarial probing of generative AI. | Scaling a manual red-team playbook into repeatable automation. |
| ✅ **[Ragas](https://github.com/explodinggradients/ragas)**<br><sub>Exploding Gradients · `Actively maintained` `Apache-2.0`</sub> | The principled choice for RAG evaluation — faithfulness, answer relevancy, context precision and recall, computed with or without ground truth. | Proving a RAG answer is actually grounded in retrieved context. |
| _+2 more in [`data/collection.json`](data/collection.json)_ | | |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-governance"></a>

## 🏛️ AI Governance Platforms

> Repos you run as part of a governance programme — model risk assessment, fairness and bias testing, explainability, drift and production monitoring, incident tracking, and audit evidence.

<sub>11 repos · 11 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| ✅ **[AI Fairness 360](https://github.com/Trusted-AI/AIF360)**<br><sub>IBM / LF AI & Data</sub> | Bias metrics and mitigation algorithms spanning pre-processing, in-processing and post-processing. | A broad menu of bias metrics when you don't yet know which one applies. |
| ✅ **[AI Incident Database](https://incidentdatabase.ai/)**<br><sub>Responsible AI Collaborative · `Continuously updated` `MIT`</sub> | Indexed, citable record of real-world AI harms — the empirical base for risk assessments that would otherwise be speculative. | Grounding a risk register in incidents that actually happened. |
| ✅ **[AI Verify & Model AI Governance Framework for GenAI](https://aiverifyfoundation.sg/)**<br><sub>IMDA Singapore · `Active` `Apache-2.0`</sub> | A governance testing framework with an actual open-source toolkit — technical tests plus process checks — rather than prose alone. | Teams that want governance claims backed by runnable tests. |
| ✅ **[Alibi Detect](https://github.com/SeldonIO/alibi-detect)**<br><sub>Seldon</sub> | Outlier, adversarial and drift detection across tabular, text and image data. | Drift and outlier detection as a monitoring control. |
| ✅ **[Captum](https://github.com/meta-pytorch/captum)**<br><sub>Meta / PyTorch</sub> | Attribution and interpretability primitives for PyTorch models. | Attribution on deep models you own the weights for. |
| ✅ **[Evidently](https://github.com/evidentlyai/evidently)**<br><sub>Evidently AI</sub> | Monitoring and reporting for data drift, data quality and model/LLM performance in production. | Catching drift after deployment, when the risk register says you must. |
| ✅ **[Fairlearn](https://github.com/fairlearn/fairlearn)**<br><sub>Fairlearn / contributors</sub> | Assesses group fairness with disaggregated metrics and applies mitigation algorithms to reduce disparity. | Measuring and mitigating disparate impact across protected groups. |
| ✅ **[InterpretML](https://github.com/interpretml/interpret)**<br><sub>InterpretML</sub> | Glassbox models plus black-box explanation techniques under one API. | Explaining a decision to someone who will not accept 'the model said so'. |
| ✅ **[Presidio](https://github.com/data-privacy-stack/presidio)**<br><sub>Microsoft</sub> | Detects and anonymises PII in text and images with configurable recognisers. | Keeping personal data out of prompts, logs and training sets. |
| ✅ **[Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)**<br><sub>Microsoft</sub> | Model debugging dashboard combining error analysis, fairness assessment, interpretability and counterfactuals in one pane. | Producing the evidence pack behind a model risk sign-off. |
| ✅ **[whylogs](https://github.com/whylabs/whylogs)**<br><sub>WhyLabs</sub> | Logs statistical profiles of data and model inputs/outputs for monitoring and audit trails. | A lightweight, privacy-preserving audit trail of what the model saw. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

---

## 📊 Coverage

| Domain | | ✅ Verified | Total |
| :----- | :-- | -: | ----: |
| 🧪 LLM, Agent & RAG Evaluation | `██████████████` | 17 | **17** |
| 🏛️ AI Governance Platforms | `█████████░░░░░` | 11 | **11** |
| **Total** | | **28** | **28** |

---

## 🤖 How this stays current

```
  data/curated.yaml  ──┐
   (human-owned)       ├──►  update_collection.py  ──►  README.md
  GitHub Search API  ──┘         (every Monday)          collection.json
```

1. A scheduled [GitHub Action](.github/workflows/update-collection.yml) runs the agent every Monday at 06:00 UTC.
2. Human-vetted repos are read from [`data/curated.yaml`](data/curated.yaml). **The agent never writes to that file** and never removes an entry from it.
3. It then scans the GitHub Search API for the topics in [`config.yaml`](config.yaml), keeping repos above **400 stars** that pass the quality gate, and scores each into its best-fitting category.
4. Discoveries land in [Candidates for review](#-candidates-for-review); they only join the main list when a human promotes them. The README is regenerated and changes are committed back.

**Tuning takes no code.** `config.yaml` controls the star threshold, search topics, domains, quality gate and blocklist. See [SETUP.md](SETUP.md).

## 🙌 Contributing

| Contribution | Why it matters |
| :----------- | :------------- |
| **Promote a 🔎 candidate to ✅** | The highest-value PR here. If you've used the tool for real, add it to `data/curated.yaml` with a `best_for` line. |
| **Flag a dead or renamed repo** | A moved or archived repo is the fastest thing to fix. |
| **Add a non-EU/US/UK/SG framework** | Coverage is thinnest outside those jurisdictions. |
| **Report a mis-sorted entry** | The categoriser scores topics; a bad score is a config fix. |

A good `best_for` line is specific. *"Evaluating LLMs"* gets rejected; *"Proving a RAG answer is grounded in retrieved context"* gets merged.

<div align="center">

**Found this useful? A ⭐ keeps it maintained and helps the next person find it.**

Released under the [MIT License](LICENSE). Framework and repository metadata belongs to its respective owners.

</div>
