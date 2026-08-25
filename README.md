<div align="center">

# 🏛️ AI Governance and Eval

**The frameworks regulators, auditors and frontier labs actually use.**

Standards, safety policies, eval harnesses and red-team tooling in one place —
each with a plain answer to *what is this* and *when would I reach for it*.

![Entries](https://img.shields.io/badge/entries-45-1f6feb?style=flat-square) ![Authoritative](https://img.shields.io/badge/authoritative-26-8957e5?style=flat-square) ![Verified tools](https://img.shields.io/badge/verified_tools-19-2da44e?style=flat-square) ![Updated](https://img.shields.io/badge/updated-2026--08--25-0969da?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-6e7781?style=flat-square)

`45 entries` · `9 categories` · auto-updated every Monday · last run 2026-08-25 05:11 UTC

</div>

---

## ⏱️ Compliance countdown

_3 deadline(s) still ahead. Recalculated every run — this is the number your programme plan is racing._

| Date | Status | What applies | Instrument |
| :--- | :----- | :----------- | :--------- |
| `2026-08-02` | ✅ **In force** | [Article 50 transparency duties + AI Office enforcement over GPAI](https://artificialintelligenceact.eu/implementation-timeline/) | EU AI Act |
| `2027-08-02` | 🟠 **342 days** | [GPAI models placed on the market before Aug 2025 must be compliant](https://artificialintelligenceact.eu/implementation-timeline/) | EU AI Act |
| `2027-12-02` | 🟢 464 days | [High-risk obligations for stand-alone systems (Annex III)](https://artificialintelligenceact.eu/implementation-timeline/) | Digital Omnibus (EU) 2026/1744 |
| `2028-08-02` | 🟢 708 days | [High-risk AI embedded in regulated products (Annex I)](https://artificialintelligenceact.eu/implementation-timeline/) | Digital Omnibus (EU) 2026/1744 |

> ⚠️ **Not legal advice.** Dates move — the Digital Omnibus shifted the
> high-risk tier in mid-2026. Verify against primary sources before
> committing budget.

---

## 🚦 Start here

_Skip the browsing. Find your row, open the thing in the last column._

| | I need to… | Open this first | Section |
| :-: | :--------- | :-------------- | :------ |
| 🇪🇺 | Ship into the EU market | **EU AI Act + Digital Omnibus** | [⚖️ Law, Regulation & Policy](#cat-regulation) |
| 🧭 | Stand up governance from zero | **NIST AI RMF** | [🧭 Risk Management & Standards](#cat-risk) |
| 📋 | Pass enterprise procurement | **ISO/IEC 42001** | [🧭 Risk Management & Standards](#cat-risk) |
| 🛡️ | Threat-model a RAG or agent app | **OWASP Top 10 for LLMs** | [🛡️ AI Security & Threat Models](#cat-security) |
| 📏 | Benchmark a base model credibly | **lm-evaluation-harness** | [🧪 Evaluation Harnesses](#cat-harness) |
| 🧪 | Run safety or agentic evals | **Inspect** | [🧪 Evaluation Harnesses](#cat-harness) |
| 🔬 | Test *your* product, not the model | **Ragas / DeepEval** | [🔬 Application & RAG Evaluation](#cat-appeval) |
| 🐙 | Attack your own endpoint first | **garak** | [🐙 Red Teaming & Adversarial Testing](#cat-redteam) |

---

## 🎯 How to read this list

Stars measure fame, not trustworthiness. Every entry carries a provenance
badge, and **the list sorts on that badge before anything else** — so a
60k-star wrapper can never outrank the EU AI Act.

| | Tier | What it means | Count |
| :-: | :--- | :------------ | ----: |
| 🏛️ | **Authoritative** | Published by a regulator, standards body or national institute. No repo, no stars, and the reason most people are here. | **26** |
| ✅ | **Verified** | Open-source tooling a human vetted and pinned in [`data/curated.yaml`](data/curated.yaml). | **19** |
| 🔎 | **Candidate** | Surfaced by the agent, unreviewed, and deliberately kept [out of the main list](#-candidates-for-review) until a human checks it. | **33** |

---

## 🏆 One pick per category

_If you read nothing else._

**⚖️ Law, Regulation & Policy**  
🏛️ [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu/) — Anyone placing an AI system or GPAI model on the EU market.

**🧭 Risk Management & Standards**  
🏛️ [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — Standing up a governance programme from zero without buying certification.

**🛡️ AI Security & Threat Models**  
🏛️ [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) — Threat modelling an LLM or RAG application in language reviewers know.

**🚨 Frontier Safety & Alignment**  
🏛️ [Responsible Scaling Policy](https://www.anthropic.com/rsp) — A worked example of pre-commitment governance with hard gates.

**🧪 Evaluation Harnesses**  
✅ [HELM (Holistic Evaluation of Language Models)](https://crfm.stanford.edu/helm/) — Arguing that a single accuracy score is not an evaluation.

**🔬 Application & RAG Evaluation**  
✅ [DeepEval](https://github.com/confident-ai/deepeval) — Regression-testing an LLM feature in an existing Python CI pipeline.

**🐙 Red Teaming & Adversarial Testing**  
✅ [garak](https://github.com/NVIDIA/garak) — A first automated red-team pass on any endpoint, in one command.

**📊 Benchmarks & Leaderboards**  
🏛️ [LMArena (Chatbot Arena)](https://lmarena.ai/) — A human-preference signal to triangulate against static benchmarks.

**📄 Transparency, Documentation & Incidents**  
🏛️ [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) — The minimum viable artefact for any model you ship.

---

## 📑 Contents

| Section | Entries | | Section | Entries |
| :------ | ------: | :-: | :------ | ------: |
| [⚖️ Law, Regulation & Policy](#cat-regulation) | 4 |  | [🔬 Application & RAG Evaluation](#cat-appeval) | 7 |
| [🧭 Risk Management & Standards](#cat-risk) | 8 |  | [🐙 Red Teaming & Adversarial Testing](#cat-redteam) | 3 |
| [🛡️ AI Security & Threat Models](#cat-security) | 5 |  | [📊 Benchmarks & Leaderboards](#cat-benchmark) | 3 |
| [🚨 Frontier Safety & Alignment](#cat-frontier) | 5 |  | [📄 Transparency, Documentation & Incidents](#cat-transparency) | 4 |
| [🧪 Evaluation Harnesses](#cat-harness) | 6 |  |  |  |

---

<a id="cat-regulation"></a>

## ⚖️ Law, Regulation & Policy

> Binding obligations and national frameworks. Deadlines here drive budget.

<sub>4 entries · 4 authoritative 🏛️ · 0 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| 🏛️ **[EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu/)**<br><sub>European Union · `EU` `In force, phased`</sub> | The world's first horizontal, risk-tiered AI law. Prohibited practices and AI-literacy duties live since Feb 2025; GPAI model obligations since Aug 2025; Article 50 transparency duties and AI Office enforcement over GPAI providers since 2 Aug 2026. | Anyone placing an AI system or GPAI model on the EU market. |
| 🏛️ **[Digital Omnibus on AI (Regulation (EU) 2026/1744)](https://artificialintelligenceact.eu/)**<br><sub>European Union · `EU` `In force since 27 Jul 2026`</sub> | Amending regulation that defers the heaviest high-risk obligations — Annex III standalone systems to 2 Dec 2027 and Annex I product-embedded systems to 2 Aug 2028 — with fixed dates, not standards-contingent triggers. Transparency and GPAI duties were untouched. | Re-planning a high-risk conformity programme that was scoped to Aug 2026. |
| 🏛️ **[Council of Europe Framework Convention on AI](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence)**<br><sub>Council of Europe · `International` `Open for signature`</sub> | First legally binding international treaty on AI, anchored in human rights, democracy and rule of law; signatories include non-European states. | Multinationals mapping obligations beyond the EU. |
| 🏛️ **[US State AI Legislation Tracker](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker/)**<br><sub>IAPP · `US` `Continuously updated`</sub> | The practical way to follow a fragmented US landscape — including Colorado, whose original AI Act was repealed and replaced by a statute signed 14 May 2026 that dropped the NIST/ISO safe harbour. | US-facing compliance teams without a 50-state law firm budget. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-risk"></a>

## 🧭 Risk Management & Standards

> Voluntary frameworks and certifiable standards — the backbone of most AI governance programmes.

<sub>8 entries · 7 authoritative 🏛️ · 1 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| 🏛️ **[NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework)**<br><sub>NIST · `US` `Voluntary, de facto US baseline`</sub> | Four functions — Govern, Map, Measure, Manage — that structure AI risk decisions across the lifecycle. Voluntary on paper, but referenced by FTC, CFPB, FDA, SEC and EEOC guidance and crosswalked to ISO/IEC 42001. | Standing up a governance programme from zero without buying certification. |
| 🏛️ **[ISO/IEC 42001 — AI Management System](https://www.iso.org/standard/42001)**<br><sub>ISO/IEC · `International` `Certifiable`</sub> | The certifiable AI management system standard (an ISO 27001 analogue for AI). Documented policies, lifecycle controls, internal audit, third-party certification. | Unblocking enterprise procurement that demands an auditable badge. |
| 🏛️ **[NIST Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)**<br><sub>NIST · `US` `Published`</sub> | Companion profile translating AI RMF functions into ~200 concrete actions for generative AI risks such as confabulation, data leakage and CBRN uplift. | Turning the abstract AI RMF into a real control list for a GenAI product. |
| 🏛️ **[ISO/IEC 23894 — AI Risk Management Guidance](https://www.iso.org/standard/77304.html)**<br><sub>ISO/IEC · `International` `Published`</sub> | Applies ISO 31000 risk management to AI; the methodology layer under an ISO/IEC 42001 management system. | Teams that already run ISO 31000 enterprise risk. |
| 🏛️ **[ISO/IEC 42005 — AI System Impact Assessment](https://www.iso.org/standard/44545.html)**<br><sub>ISO/IEC · `International` `Published`</sub> | Guidance for documenting impacts of AI systems on individuals and society — the closest ISO analogue to a fundamental rights impact assessment. | Building an FRIA/DPIA-adjacent artefact that survives audit. |
| 🏛️ **[NIST CAISI & AI Agent Standards Initiative](https://www.nist.gov/caisi)**<br><sub>NIST CAISI · `US` `Active, guidance emerging`</sub> | The US centre for AI standards; launched an AI Agent Standards Initiative in Feb 2026, with agentic threat surface covered in NIST AI 100-2 and draft NIST IR 8596 mapping cyber functions to AI risk. | Anyone shipping autonomous agents into a regulated US environment. |
| 🏛️ **[OECD AI Principles & Policy Observatory](https://oecd.ai/)**<br><sub>OECD · `International` `Adopted, widely referenced`</sub> | The intergovernmental principles most other regimes cite, plus a live observatory of national AI policies and a shared AI incident monitor. | Baseline vocabulary that maps cleanly onto EU, US and G7 texts. |
| ✅ **[AI Verify & Model AI Governance Framework for GenAI](https://aiverifyfoundation.sg/)**<br><sub>IMDA Singapore · `Singapore` `Active` `Apache-2.0`</sub> | A governance testing framework with an actual open-source toolkit — technical tests plus process checks — rather than prose alone. | Teams that want governance claims backed by runnable tests. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-security"></a>

## 🛡️ AI Security & Threat Models

> Attack taxonomies, control catalogues, and defences for AI-specific threats.

<sub>5 entries · 5 authoritative 🏛️ · 0 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| 🏛️ **[OWASP Top 10 for LLM Applications](https://genai.owasp.org/)**<br><sub>OWASP GenAI Security Project · `Actively maintained`</sub> | The common language for LLM application risk — prompt injection, insecure output handling, supply chain, excessive agency — plus companion guides for agentic threats and red teaming. | Threat modelling an LLM or RAG application in language reviewers know. |
| 🏛️ **[MITRE ATLAS](https://atlas.mitre.org/)**<br><sub>MITRE · `Actively maintained`</sub> | ATT&CK-style knowledge base of real-world adversary tactics and techniques against AI systems, with case studies and mitigations. | Mapping detections and red-team scope to named adversary behaviours. |
| 🏛️ **[CSA AI Controls Matrix (AICM)](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix)**<br><sub>Cloud Security Alliance · `Published`</sub> | Control catalogue for AI systems in cloud environments, with mappings to ISO/IEC 42001, NIST AI RMF and the EU AI Act. | Answering vendor security questionnaires without reinventing controls. |
| 🏛️ **[Google Secure AI Framework (SAIF)](https://saif.google/)**<br><sub>Google · `Active`</sub> | Six-element security framework for AI, with a self-assessment that produces a risk report rather than a checklist. | A fast, opinionated security baseline for an AI platform team. |
| 🏛️ **[NIST AI 100-2 — Adversarial ML Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)**<br><sub>NIST · `US` `Published`</sub> | Standardised taxonomy of adversarial machine learning attacks and mitigations; the March 2025 edition names AI agents as a threat surface. | Precise vocabulary for evasion, poisoning and extraction attacks. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-frontier"></a>

## 🚨 Frontier Safety & Alignment

> Capability thresholds, pre-deployment commitments, and alignment research infrastructure.

<sub>5 entries · 5 authoritative 🏛️ · 0 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| 🏛️ **[Responsible Scaling Policy](https://www.anthropic.com/rsp)**<br><sub>Anthropic · `Active`</sub> | AI Safety Levels tied to capability thresholds, with defined safeguards that must be in place before a model crossing a threshold is deployed. | A worked example of pre-commitment governance with hard gates. |
| 🏛️ **[Frontier Model Forum](https://www.frontiermodelforum.org/)**<br><sub>FMF · `Active`</sub> | Industry body publishing technical reports on frontier capability assessments, safety frameworks and third-party assessment norms. | Tracking where cross-lab safety practice is converging. |
| 🏛️ **[Frontier Safety Framework](https://deepmind.google/discover/blog/introducing-the-frontier-safety-framework/)**<br><sub>Google DeepMind · `Active`</sub> | Critical Capability Levels with early-warning evaluations and mitigation commitments triggered before capability is reached. | Designing early-warning evals rather than post-hoc testing. |
| 🏛️ **[International AI Safety Report](https://internationalaisafetyreport.org/)**<br><sub>Chaired by Yoshua Bengio · `International` `Annual + updates`</sub> | The IPCC-style scientific consensus report on advanced AI capability and risk, backed by ~30 countries plus the EU, OECD and UN. | A citable evidence base for board and regulator briefings. |
| 🏛️ **[Preparedness Framework](https://openai.com/preparedness/)**<br><sub>OpenAI · `Active`</sub> | Tracked capability categories with thresholds and required safeguards before deployment or further scaling. | Comparing how labs define and measure dangerous capability. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-harness"></a>

## 🧪 Evaluation Harnesses

> Run benchmarks and safety evals reproducibly, across models.

<sub>6 entries · 0 authoritative 🏛️ · 6 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| ✅ **[HELM (Holistic Evaluation of Language Models)](https://crfm.stanford.edu/helm/)**<br><sub>Stanford CRFM · `Actively maintained` `Apache-2.0`</sub> | Multi-metric evaluation by design — accuracy, calibration, robustness, bias, toxicity, efficiency — with public leaderboards across domain variants. | Arguing that a single accuracy score is not an evaluation. |
| ✅ **[Inspect](https://inspect.aisi.org.uk/)**<br><sub>UK AI Security Institute · `Actively maintained` `MIT`</sub> | The evaluation framework a national safety institute uses on frontier models — solvers, scorers, tool use, multi-turn agents and human-in-the-loop, with a proper log viewer. | Safety and agentic evals you need to defend to an auditor. |
| ✅ **[LightEval](https://github.com/huggingface/lighteval)**<br><sub>Hugging Face · `Actively maintained` `MIT`</sub> | Lightweight, backend-agnostic evaluation pipeline used in leaderboard-style runs; easy to point at vLLM, TGI or an inference endpoint. | Fast iteration when a full harness is too heavy. |
| ✅ **[LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)**<br><sub>EleutherAI · `Actively maintained` `MIT`</sub> | The de facto standard for reproducible academic benchmarking; hundreds of tasks behind one interface, and the harness most published numbers come from. | Reporting MMLU/HellaSwag-class numbers others can reproduce. |
| ✅ **[METR Task Standard](https://github.com/METR/task-standard)**<br><sub>METR · `Stable, low activity` `MIT`</sub> | A specification for defining autonomous-capability tasks portably, so dangerous-capability evaluations can be shared and re-run across organisations. | Writing agent tasks that another lab can execute unchanged. |
| ✅ **[OpenCompass](https://github.com/open-compass/opencompass)**<br><sub>Shanghai AI Laboratory · `Actively maintained` `Apache-2.0`</sub> | Large bilingual (EN/CN) benchmark platform with broad dataset and model coverage, including domain suites for finance, healthcare and law. | Non-English and domain-specific coverage the Western harnesses miss. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-appeval"></a>

## 🔬 Application & RAG Evaluation

> Evaluate your own product, not the base model.

<sub>7 entries · 0 authoritative 🏛️ · 7 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| ✅ **[DeepEval](https://github.com/confident-ai/deepeval)**<br><sub>Confident AI · `Actively maintained` `Apache-2.0`</sub> | Pytest-style evaluation for LLM apps — G-Eval, hallucination, task completion and custom metrics that fail a CI build like any other test. | Regression-testing an LLM feature in an existing Python CI pipeline. |
| ✅ **[Giskard](https://github.com/Giskard-AI/giskard)**<br><sub>Giskard AI · `Actively maintained` `Apache-2.0`</sub> | Automated vulnerability scanning for ML and LLM apps — hallucination, bias, prompt injection, harmfulness — with reports oriented to EU AI Act evidence. | Generating compliance-shaped evidence from an automated scan. |
| ✅ **[Langfuse](https://github.com/langfuse/langfuse)**<br><sub>Langfuse · `Actively maintained` `MIT (core)`</sub> | Open-source LLM observability with datasets, scores, prompt management and human annotation queues; framework-agnostic. | Self-hosted production tracing with an evaluation loop attached. |
| ✅ **[Phoenix](https://github.com/Arize-ai/phoenix)**<br><sub>Arize AI · `Actively maintained` `Elastic-2.0`</sub> | Self-hostable, OpenTelemetry-native tracing and evaluation — traces become datasets, datasets become evals. | Observability and eval in one place, on your own infrastructure. |
| ✅ **[promptfoo](https://github.com/promptfoo/promptfoo)**<br><sub>promptfoo · `Actively maintained` `MIT`</sub> | Declarative YAML matrix testing across prompts, providers and assertions, with a strong adversarial/red-team generator. Note - reported in 2026 to be acquired by OpenAI; still MIT-licensed, but weigh vendor neutrality. | A/B testing a prompt or provider change without writing a harness. |
| ✅ **[Ragas](https://github.com/explodinggradients/ragas)**<br><sub>Exploding Gradients · `Actively maintained` `Apache-2.0`</sub> | The principled choice for RAG evaluation — faithfulness, answer relevancy, context precision and recall, computed with or without ground truth. | Proving a RAG answer is actually grounded in retrieved context. |
| ✅ **[TruLens](https://github.com/truera/trulens)**<br><sub>Snowflake · `Actively maintained` `MIT`</sub> | Feedback-function approach to RAG and agent evaluation, with a native Snowflake path for enterprises already on that stack. | Snowflake-resident data and governance requirements. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-redteam"></a>

## 🐙 Red Teaming & Adversarial Testing

> Automated probes, jailbreak suites, and attack libraries you point at your own endpoint.

<sub>3 entries · 0 authoritative 🏛️ · 3 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| ✅ **[garak](https://github.com/NVIDIA/garak)**<br><sub>NVIDIA · `Actively maintained` `Apache-2.0`</sub> | An LLM vulnerability scanner in the nmap tradition — dozens of probes for jailbreaks, prompt injection, data leakage, toxicity and encoding attacks. | A first automated red-team pass on any endpoint, in one command. |
| ✅ **[Purple Llama / CyberSecEval](https://github.com/meta-llama/PurpleLlama)**<br><sub>Meta · `Active` `Custom`</sub> | Cybersecurity safety evaluations plus input/output guard models (Llama Guard, Code Shield) for insecure-code and attack-compliance testing. | Measuring whether a coding assistant emits insecure code. |
| ✅ **[PyRIT](https://github.com/microsoft/PyRIT)**<br><sub>Microsoft · `Actively maintained` `MIT`</sub> | Python Risk Identification Toolkit — orchestrators, converters and scorers for automating multi-turn adversarial probing of generative AI. | Scaling a manual red-team playbook into repeatable automation. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-benchmark"></a>

## 📊 Benchmarks & Leaderboards

> Comparative capability signals. Directional, not decisive.

<sub>3 entries · 2 authoritative 🏛️ · 1 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| 🏛️ **[LMArena (Chatbot Arena)](https://lmarena.ai/)**<br><sub>LMArena / UC Berkeley · `Live`</sub> | Pairwise human preference at scale via blind A/B voting, reported as Elo. Measures preference, not correctness — and is gameable by style. | A human-preference signal to triangulate against static benchmarks. |
| 🏛️ **[Epoch AI Benchmarking Hub](https://epoch.ai/data)**<br><sub>Epoch AI · `Continuously updated`</sub> | Independent, methodologically careful tracking of model capability, compute and trends, with data and methodology published openly. | Trend claims that will survive scrutiny. |
| ✅ **[SWE-bench](https://www.swebench.com/)**<br><sub>Princeton NLP · `Active` `MIT`</sub> | Real GitHub issues resolved against real repositories, graded by whether the test suite passes — the reference agentic coding benchmark. | Evaluating coding agents on work that resembles the actual job. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

<a id="cat-transparency"></a>

## 📄 Transparency, Documentation & Incidents

> Model cards, transparency indices, provenance, and incident evidence bases.

<sub>4 entries · 3 authoritative 🏛️ · 1 verified ✅</sub>

| Entry | What it is | Reach for it when |
| :---- | :--------- | :---------------- |
| 🏛️ **[Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)**<br><sub>Google Research · `Foundational`</sub> | The original documentation pattern — intended use, out-of-scope use, disaggregated performance, ethical considerations. Now referenced by ISO/IEC 42001 and the EU AI Act's documentation duties. | The minimum viable artefact for any model you ship. |
| 🏛️ **[Datasheets for Datasets](https://arxiv.org/abs/1803.09010)**<br><sub>Gebru et al. · `Foundational`</sub> | Structured documentation of dataset motivation, composition, collection and recommended uses — the dataset counterpart to a model card. | Data provenance evidence that auditors will ask for. |
| 🏛️ **[Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/)**<br><sub>Stanford CRFM · `Periodic`</sub> | Scores major developers across ~100 transparency indicators covering data, labour, compute, capability and downstream use. | Benchmarking your own disclosure against the field. |
| ✅ **[AI Incident Database](https://incidentdatabase.ai/)**<br><sub>Responsible AI Collaborative · `Continuously updated` `MIT`</sub> | Indexed, citable record of real-world AI harms — the empirical base for risk assessments that would otherwise be speculative. | Grounding a risk register in incidents that actually happened. |

<div align="right"><a href="#-contents"><sub>back to contents ↑</sub></a></div>

---

## 🔎 Candidates for review

**33 projects** the agent found on the configured GitHub topics that **no human has vetted**. They sit here rather than in the categories above because a GitHub topic is self-declared — anyone shipping an agent product can tag it `ai-safety`. Treat these as leads to investigate, not recommendations.

> 💡 **Used one of these in anger?** That's the most valuable PR you can open: move it into [`data/curated.yaml`](data/curated.yaml) with a `best_for` line and today's date, and it joins the real list.

<details>
<summary><b>Show 33 unreviewed candidates</b></summary>

| Project | Stars | Suggested category | Description |
| :------ | ----: | :----------------- | :---------- |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | ⭐ 27.7k | 🔬 Application & RAG Evaluation | The open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes... |
| [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) | ⭐ 20.9k | 🧭 Risk Management & Standards | A curated list of awesome open source libraries to deploy, monitor, version and scale your machine learning |
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | ⭐ 11.3k | 🧭 Risk Management & Standards | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in... |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | ⭐ 10.6k | ⚖️ Law, Regulation & Policy | Graph-Native Infrastructure for Context and Accountable AI Systems |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | ⭐ 6.1k | ⚖️ Law, Regulation & Policy | AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliabilit... |
| [Giskard-AI/giskard-oss](https://github.com/Giskard-AI/giskard-oss) | ⭐ 5.8k | 🛡️ AI Security & Threat Models | 🐢 Open-Source Evaluation & Testing library for LLM Agents |
| [iflytek/skillhub](https://github.com/iflytek/skillhub) | ⭐ 4.9k | ⚖️ Law, Regulation & Policy | Self-hosted, open-source agent skill registry for enterprises. Publish & version skill packages, govern wit... |
| [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) | ⭐ 4.1k | 🔍 Interpretability & Explainability | A curated list of awesome responsible machine learning resources. |
| [fairlearn/fairlearn](https://github.com/fairlearn/fairlearn) | ⭐ 2.3k | ⚖️ Fairness, Bias & Privacy | A Python package to assess and improve fairness of machine learning models. |
| [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | ⭐ 2.2k | ⚖️ Law, Regulation & Policy | The Enterprise Architecture Governance Harness — strategy, architecture, delivery, and assurance using AI c... |
| [valqore/valqore](https://github.com/valqore/valqore) | ⭐ 1.8k | 🚨 Frontier Safety & Alignment | Safety-first guardrails for AI-driven cloud and Kubernetes operations |
| [microsoft/responsible-ai-toolbox](https://github.com/microsoft/responsible-ai-toolbox) | ⭐ 1.8k | 🔍 Interpretability & Explainability | Responsible AI Toolbox is a suite of tools providing model and data exploration and assessment user interfa... |
| [PKU-Alignment/safe-rlhf](https://github.com/PKU-Alignment/safe-rlhf) | ⭐ 1.6k | 🚨 Frontier Safety & Alignment | Safe RLHF: Constrained Value Alignment via Safe Reinforcement Learning from Human Feedback |
| [lynote-ai/humanize-text](https://github.com/lynote-ai/humanize-text) | ⭐ 1.6k | 🧭 Risk Management & Standards | Open-source pipeline and reference implementations for improving the readability and natural cadence of AI-... |
| [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) | ⭐ 1.5k | 🚧 Guardrails & Runtime Controls | An AI coding agent guardrail — a CLI hook that blocks destructive git and filesystem commands and secret fi... |
| [ModelOriented/DALEX](https://github.com/ModelOriented/DALEX) | ⭐ 1.5k | 🔍 Interpretability & Explainability | moDel Agnostic Language for Exploration and eXplanation |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | ⭐ 1.2k | 🚨 Frontier Safety & Alignment | [JMLR 2026] "UQLM: A Python Package for Uncertainty Quantification in Large Language Models" |
| [ZhangJinHaHaHa/AgentLens](https://github.com/ZhangJinHaHaHa/AgentLens) | ⭐ 1k | 🚨 Frontier Safety & Alignment | Agentlens is a trusted agent trading platform.  Here, you can quickly find the Agent that meets your needs,... |
| [microsoft/rag-time](https://github.com/microsoft/rag-time) | ⭐ 898 | 🧭 Risk Management & Standards | RAG Time: A 5-week Learning Journey to Mastering RAG |
| [chrisliu298/awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) | ⭐ 623 | 🧭 Risk Management & Standards | A resource repository for machine unlearning in large language models |
| [PacificAI/langtest](https://github.com/PacificAI/langtest) | ⭐ 559 | 🧭 Risk Management & Standards | Deliver safe & effective language models |
| [secureagentics/Adrian](https://github.com/secureagentics/Adrian) | ⭐ 548 | 🛡️ AI Security & Threat Models | Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use,... |
| [h5i-dev/h5i](https://github.com/h5i-dev/h5i) | ⭐ 540 | 🛡️ AI Security & Threat Models | Sandboxed collaboration for multi-agent teams: a Git-backed message forum with each agent isolated in its o... |
| [decionis/agent-safe-pipeline](https://github.com/decionis/agent-safe-pipeline) | ⭐ 534 | ⚖️ Law, Regulation & Policy | Reference architecture for AI agents that propose actions but cannot authorize them — immutable intent capt... |
| [aisa-group/PostTrainBench](https://github.com/aisa-group/PostTrainBench) | ⭐ 529 | 🚨 Frontier Safety & Alignment | Measuring how well CLI agents like Claude Code or Codex CLI can post-train base LLMs on a single H100 GPU i... |
| [agencyenterprise/PromptInject](https://github.com/agencyenterprise/PromptInject) | ⭐ 519 | 🚨 Frontier Safety & Alignment | PromptInject is a framework that assembles prompts in a modular fashion to provide a quantitative analysis... |
| [Floe-Labs/floe-guard](https://github.com/Floe-Labs/floe-guard) | ⭐ 516 | 🚨 Frontier Safety & Alignment | The spend meter and budget gate for AI voice agents. Meters STT + TTS + LLM + telephony per call, out of th... |
| [cordum-io/cordum](https://github.com/cordum-io/cordum) | ⭐ 496 | ⚖️ Law, Regulation & Policy | The action firewall for AI agents. Enforce policy and human approval before risky tool calls, shell command... |
| [RiccardoBiosas/awesome-MLSecOps](https://github.com/RiccardoBiosas/awesome-MLSecOps) | ⭐ 457 | 🛡️ AI Security & Threat Models | A curated list of MLSecOps tools and resources for securing machine learning and AI systems - adversarial M... |
| [lynote-ai/ai-text-detector](https://github.com/lynote-ai/ai-text-detector) | ⭐ 438 | 🔍 Interpretability & Explainability | A cautious, explainable AI-like text risk analyzer for local workflows and coding agents. |
| [xpert-ai/xpert](https://github.com/xpert-ai/xpert) | ⭐ 433 | ⚖️ Law, Regulation & Policy | XpertAI is an open-source platform for building, running, and evolving ai agents, providing extensible capa... |
| [pegasi-ai/reins](https://github.com/pegasi-ai/reins) | ⭐ 408 | 🚨 Frontier Safety & Alignment | Stop AI agents from doing things you didn't ask for. |
| [Varietyz/Disciplined-AI-Software-Development](https://github.com/Varietyz/Disciplined-AI-Software-Development) | ⭐ 405 | ⚖️ Law, Regulation & Policy | A disciplined methodology for AI-assisted software development. Covers architectural constraints, validatio... |

</details>

---

## 📊 Coverage

| Section | | 🏛️ | ✅ | Total |
| :------ | :-- | -: | -: | ----: |
| ⚖️ Law, Regulation & Policy | `███████░░░░░░░` | 4 | 0 | **4** |
| 🧭 Risk Management & Standards | `██████████████` | 7 | 1 | **8** |
| 🛡️ AI Security & Threat Models | `█████████░░░░░` | 5 | 0 | **5** |
| 🚨 Frontier Safety & Alignment | `█████████░░░░░` | 5 | 0 | **5** |
| 🧪 Evaluation Harnesses | `██████████░░░░` | 0 | 6 | **6** |
| 🔬 Application & RAG Evaluation | `████████████░░` | 0 | 7 | **7** |
| 🐙 Red Teaming & Adversarial Testing | `█████░░░░░░░░░` | 0 | 3 | **3** |
| 📊 Benchmarks & Leaderboards | `█████░░░░░░░░░` | 2 | 1 | **3** |
| 📄 Transparency, Documentation & Incidents | `███████░░░░░░░` | 3 | 1 | **4** |
| **Total** | | **26** | **19** | **45** |

---

## 🤖 How this stays current

```
  data/curated.yaml  ──┐
   (human-owned)       ├──►  update_collection.py  ──►  README.md
  GitHub Search API  ──┘         (every Monday)          collection.json
```

1. A scheduled [GitHub Action](.github/workflows/update-collection.yml) runs the agent every Monday at 06:00 UTC.
2. Authoritative frameworks and vetted tools are read from [`data/curated.yaml`](data/curated.yaml). **The agent never writes to that file** and never removes an entry from it.
3. It then scans the GitHub Search API for the topics in [`config.yaml`](config.yaml), keeping repos above **400 stars** that pass the quality gate, and scores each into its best-fitting category.
4. Discoveries land in [Candidates for review](#-candidates-for-review); they only join the main list when a human promotes them. Deadlines are recalculated, the README is regenerated, and changes are committed back.

**Tuning takes no code.** `config.yaml` controls the star threshold, search topics, categories, quality gate, blocklist and deadlines. See [SETUP.md](SETUP.md).

## 🙌 Contributing

| Contribution | Why it matters |
| :----------- | :------------- |
| **Promote a 🔎 candidate to ✅** | The highest-value PR here. If you've used the tool for real, add it to `data/curated.yaml` with a `best_for` line. |
| **Fix a moved deadline or status** | Cite the primary source and it merges fast. |
| **Add a non-EU/US/UK/SG framework** | Coverage is thinnest outside those jurisdictions. |
| **Report a mis-sorted entry** | The categoriser scores topics; a bad score is a config fix. |

A good `best_for` line is specific. *"Evaluating LLMs"* gets rejected; *"Proving a RAG answer is grounded in retrieved context"* gets merged.

<div align="center">

**Found this useful? A ⭐ keeps it maintained and helps the next person find it.**

Released under the [MIT License](LICENSE). Framework and repository metadata belongs to its respective owners.

</div>
