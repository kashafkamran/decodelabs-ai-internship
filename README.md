<div align="center">

# DecodeLabs AI Internship Projects
### Batch 2026 | Industrial Training Kit

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/DecodeLabs-AI%20Internship-purple?style=for-the-badge)

<br/>

> *"Before you build systems that learn on their own, you must master the art of  
> teaching a machine through explicit logic,and then let the data speak."*  
> DecodeLabs, Batch 2026

</div>

---

## 👩‍💻 About This Repository

This repository documents my complete AI Engineering journey at **DecodeLabs** as part of the **Batch 2026 Industrial Training Kit**. It contains three progressive projects that build on each other — starting from deterministic rule-based logic, advancing to supervised machine learning, and culminating in a real-world recommendation engine.

Every project follows the **IPO (Input → Process → Output) architectural framework** and is built to professional standards — modular code, full documentation, reproducible results, verified outputs, and presentation-ready visualizations.

---

## 🗂️ Repository Structure

```
DecodeLabs-AI-Internship/
│
├── Project_1_Rule_Based_Chatbot/
│   ├── chatbot.py              ← Main entry point & IPO orchestrator
│   ├── knowledge_base.py       ← Single source of truth for all intents
│   ├── utils.py                ← Colors, display, formatting, stats
│   ├── logger.py               ← Session logging & audit trail
│   ├── requirements.txt        ← Dependencies
│   └── chat_logs/              ← Auto-generated timestamped session logs
│
├── Project_2_Iris_Classifier/
│   └── DecodeLabs_P2_Iris_Classifier.ipynb
│
├── Project_3_TechStack_Recommender/
│   └── DecodeLabs_P3_TechStack_Recommender.ipynb
│
└── README.md
```

---

## 📁 Project 1 — Rule-Based AI Chatbot (ARIA)

<div align="center">

![Project1](https://img.shields.io/badge/Type-Rule--Based%20AI-blue?style=flat-square)
![Tool](https://img.shields.io/badge/Tool-VS%20Code-007ACC?style=flat-square&logo=visual-studio-code)
![Language](https://img.shields.io/badge/Language-Python%203.14-blue?style=flat-square&logo=python)
![Tested](https://img.shields.io/badge/Tested-Verified%20✓-success?style=flat-square)

</div>

### 🎯 Goal
Build a terminal-based conversational AI agent — **ARIA (Automated Rule-based Intelligence Assistant)** — that responds to user inputs using deterministic rule-based logic. This is the same control layer architecture used in production AI guardrail systems like NVIDIA NeMo and Llama Guard.

### 🏗️ Architecture
```
INPUT   →  Raw user text
            Phase 1: Sanitization (.lower() + .strip() + punctuation removal)
            Handles: HELLO / hello / " hello " / Hello!!! → all → "hello"
            ↓
PROCESS →  3-Tier Intent Matching Engine
            Tier 1: Exact Match    → O(1) Dictionary .get() lookup
            Tier 2: Keyword Scan   → Partial match inside sentences
            Tier 3: Fallback       → Random rotating response pool
            ↓
OUTPUT  →  Color-coded terminal response
            Match type label [EXACT / KEYWORD / SYSTEM / FALLBACK]
            Real-time session statistics tracking
            Timestamped audit log written to chat_logs/
```

### ✅ Key Requirements Met
| Requirement | Implementation |
|---|---|
| Handle greetings & exit commands | 40+ exact intents + EXIT_COMMANDS set (O(1) lookup) |
| Use if-else logic for responses | O(1) dictionary `.get()` — anti-pattern if-elif avoided |
| Run in a continuous loop | `while True` heartbeat with graceful kill command |
| Input sanitization | `.lower().strip()` + punctuation removal + space collapse |
| Fallback for unknowns | `random.choice()` pool — 4 rotating messages, never repetitive |

### 🔑 Professional Features Built
- **Modular 4-file architecture** — each file has exactly one responsibility; adding new intents requires touching only `knowledge_base.py`
- **O(1) dictionary lookup** — explicitly chosen over O(n) if-elif ladder as highlighted in the project specification
- **3-tier matching engine** — Exact → Keyword → Fallback, fully tested and verified
- **Special command handler** — `time`, `date`, `clear` handled separately from static dictionary (live data can't be stored as strings)
- **Rotating fallback responses** — `random.choice()` across 4 messages so repeated unknowns never feel identical
- **In-memory session statistics** — dictionary tracking `total_messages`, `exact_matches`, `keyword_matches`, `fallbacks` throughout session
- **Color-coded terminal output** — Cyan (matched), Red (fallback), Yellow (system), Magenta (headers)
- **Timestamped session logger** — every exchange saved with `[HH:MM:SS] [MATCH_TYPE]` labels — traceability as specified in slides
- **Session summary on exit** — total messages, match breakdown, duration printed and written to log
- **Graceful Ctrl+C handling** — `KeyboardInterrupt` caught, clean shutdown instead of crash

### 🐛 Known Limitation Documented
During testing, a substring collision edge case was identified and documented:

```
Input : "tell me something random"
Result: KEYWORD match on "hi" (found inside "t-hi-ng")
```
This is a known limitation of raw substring matching — the same reason production NLP systems use tokenization instead. Identified, explained, and noted as a natural upgrade path to Project 3.

### 📊 Verified Test Results
```
✅ "hello"          → EXACT    (sanitization: lowercase)
✅ "HELLO"          → EXACT    (sanitization: uppercase)
✅ "  hello  "      → EXACT    (sanitization: whitespace)
✅ "Hello!!!"       → EXACT    (sanitization: punctuation)
✅ "I feel happy today" → KEYWORD (partial sentence matching)
✅ "what is ai"     → EXACT    (multi-word intent)
✅ "time"           → SYSTEM   (live data command)
✅ "date"           → SYSTEM   (live data command)
✅ "clear"          → SYSTEM   (screen control)
✅ "banana"         → FALLBACK (unrecognized input)
✅ "quantum physics" → FALLBACK (out-of-scope query)
✅ "asdfghjkl"      → FALLBACK (gibberish input)
✅ "quit"           → EXIT     (clean session termination)
Total: 14 messages | 8 Exact | 2 Keyword | 0 Fallback (in demo session)
```

### 📦 Tech Stack
```
Python 3.14   Colorama   datetime   random   os
```

### ▶️ How to Run
```bash
pip install colorama
python chatbot.py
```

### 🖥️ Sample Session Output
```
  🤖 ARIA ▸  Hello! I'm ARIA — your Rule-Based AI Assistant.

  You ▸  what is machine learning
  🤖 ARIA ▸  ML is a subset of AI where systems learn from data...
  ⚙  [Match: EXACT]
  ────────────────────────────────────────────────────────────

  SESSION SUMMARY
  ═══════════════════════════════════════════════════════════
  Total Messages Sent   :  14
  Matched (Exact)       :  8
  Matched (Keyword)     :  2
  Unmatched (Fallback)  :  0
  Session Duration      :  8m 12s
  ═══════════════════════════════════════════════════════════
```

---

## 📁 Project 2 — Data Classification Using AI

<div align="center">

![Project2](https://img.shields.io/badge/Type-Supervised%20Learning-orange?style=flat-square)
![Tool](https://img.shields.io/badge/Tool-Google%20Colab-F9AB00?style=flat-square&logo=google-colab)
![Algorithm](https://img.shields.io/badge/Algorithm-KNN-green?style=flat-square)
![Tested](https://img.shields.io/badge/Tested-Verified%20✓-success?style=flat-square)

</div>

### 🎯 Goal
Build a complete supervised machine learning pipeline that trains, evaluates, and deploys a KNN classifier on the Iris benchmark dataset — demonstrating the full journey from raw data exploration to live flower species prediction with confidence breakdown.

### 🏗️ Architecture
```
INPUT   →  Iris Dataset (150 samples | 3 classes | 4 features)
            EDA: shape, class distribution, statistical summary
            Pairplot + Correlation Heatmap
            StandardScaler (fit on train only — no data leakage)
            80/20 Stratified Train-Test Split with shuffle
            ↓
PROCESS →  Elbow Method: K=1 to K=20 → error rate per K → optimal K
            KNN Classifier (n_neighbors=optimal_k, metric=euclidean)
            Instantiate → Fit → Predict (3-step sklearn workflow)
            ↓
OUTPUT  →  Confusion Matrix (per-class TP/FP/FN breakdown)
            Full Classification Report (Precision, Recall, F1)
            Weighted F1 Score (primary honest metric)
            Model Comparison: KNN vs Logistic Regression (bar chart)
            Live Flower Species Predictor with confidence bar display
```

### ✅ Key Requirements Met
| Requirement | Implementation |
|---|---|
| Load and understand dataset | Full EDA with shape, distribution, stats, pairplot, heatmap |
| Split into train/test sets | 80/20 stratified split with `shuffle=True` and `random_state=42` |
| Apply classification algorithm | KNN via Scikit-learn with programmatically selected optimal K |
| Feature scaling | StandardScaler — fitted on train only, transformed on both |
| Confusion Matrix | Per-class TP, FP, FN breakdown with heatmap visualization |
| F1 Score | Weighted F1 as primary metric — explicitly avoids accuracy mirage |

### 🔑 Professional Features Built
- **Elbow Method visualization** — tests K=1 to K=20, plots error curve, highlights optimal K with red dashed line — no manual guessing
- **Data leakage prevention** — `scaler.fit_transform(X_train)` then `scaler.transform(X_test)` only — never fit on test data
- **Stratified split** — `stratify=y` ensures all 3 classes proportionally represented in both sets
- **F1 Score over accuracy** — slides explicitly warned against "accuracy mirage"; F1 balances precision and recall
- **5 professional visualizations:**
  - Pairplot — all feature combinations colored by species
  - Correlation heatmap — feature relationship analysis
  - Elbow curve — optimal K selection with annotation
  - Confusion matrix — heatmap with per-cell values
  - Model comparison bar chart — KNN vs Logistic Regression side by side
- **Live flower predictor** — enter 4 measurements → get species + confidence breakdown with `█░` visual bars for all 3 classes
- **Model comparison** — KNN benchmarked against Logistic Regression with accuracy and F1 both compared
- **Full reproducibility** — `RANDOM_STATE = 42` applied consistently across all operations

### 📊 Results
```
Optimal K             :  5
Model Accuracy        :  96.67%
Weighted F1 Score     :  96.67%
Setosa Precision      :  100%  (perfectly separated)
Versicolor F1         :  94%
Virginica F1          :  97%
KNN vs LR Comparison  :  Both models perform within 1-2% — KNN selected
                          as it requires no assumptions about data distribution
```

### 📦 Tech Stack
```
Python   Scikit-learn   Pandas   NumPy   Matplotlib   Seaborn
Google Colab
```

---
## 📁 Project 3 — AI Recommendation Logic

<div align="center">

![Project3](https://img.shields.io/badge/Type-Recommendation%20Engine-purple?style=flat-square)
![Tool](https://img.shields.io/badge/Tool-Google%20Colab-F9AB00?style=flat-square&logo=google-colab)
![Algorithm](https://img.shields.io/badge/Algorithm-Cosine%20Similarity-red?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-1000%20Candidates-blue?style=flat-square)
![Roles](https://img.shields.io/badge/Job%20Roles-20+-orange?style=flat-square)

</div>

### 🎯 Goal
Build a **Tech Stack Recommender** — a content-based filtering engine that maps a user's raw skills to the most relevant tech career paths using TF-IDF vectorization and Cosine Similarity. Role profiles are **learned from 1000 real candidate records** in `candidate_job_role_dataset.csv`. The same foundational logic powering recommendation engines at Netflix, Amazon, and Spotify.

### 🏗️ Architecture
```
INPUT   →  candidate_job_role_dataset.csv (1000 candidates | 20+ roles)
            Skills aggregated per role → rich role profile per job title
            User skills normalized (spaces → underscores)
            TF-IDF vectorization using pre-fitted vocabulary space
            ↓
PROCESS →  4-Step Ranking Pipeline:
            Step 1: Ingestion  → Capture & clean user skills → vector
            Step 2: Scoring    → Cosine Similarity vs all 20+ role vectors
            Step 3: Sorting    → Rank all roles by score descending
            Step 4: Filtering  → Truncate to Top-N (prevents choice overload)
            ↓
OUTPUT  →  Ranked career recommendations with similarity scores
            Experience level filter (Entry / Mid / Senior)
            Skill gap analysis (matched / missing / bonus skills)
            Cold start fallback (popular roles for empty profiles)
            Multi-user side-by-side comparison visualization
```

### ✅ Key Requirements Met
| Requirement | Implementation |
|---|---|
| Take user input (min 3) | Onboarding ingestion with vocabulary normalization |
| Match using similarity logic | Cosine Similarity — magnitude-invariant, industry standard |
| Display recommended items | Top-N ranked list with scores and candidate counts |
| Content-based filtering | TF-IDF on 20+ roles learned from 1000 real candidates |
| Cold start handling | Popular roles fallback — no crash on empty input |

### 🔑 Professional Features Built
- **Real dataset** — role profiles built by aggregating 1000 real candidate records from `candidate_job_role_dataset.csv`, not manually hardcoded
- **TF-IDF over binary matching** — penalizes generic skills (python, sql, javascript) appearing across many roles, rewards specific ones (solidity, siem, unreal_engine) — mathematically derived weights, not guessed
- **Cosine Similarity over Euclidean** — explicitly chosen because Euclidean is magnitude-sensitive; a role profile built from 50 candidates will always have a larger vector than one from 10, making it seem artificially closer. Cosine measures angular alignment only
- **4-step pipeline** — Ingestion → Scoring → Sorting → Filtering, exactly as specified in slides
- **Experience level filter** — recommendations can be filtered by Entry / Mid / Senior derived from real candidate data
- **20+ real job roles** including: Data Scientist, AIML Engineer, Frontend Developer, Backend Developer, Full Stack Python/Java Developer, DevOps Engineer, Kubernetes Operations Engineer, Cybersecurity Engineer, Mobile Developer, Blockchain Developer, Data Analyst, Designer, Web Developer, Game Developer, Software Project Manager, and more
- **Skill vocabulary extracted automatically** — unique skills discovered from the dataset, not pre-defined
- **Skill Gap Analyzer** — gaps calculated from real candidate data: ✅ skills you have, ❌ skills to learn, 💡 bonus skills you bring
- **Cold Start Handler** — falls back to most popular roles by candidate count, no crash, no zero-vector error
- **Multi-user comparison chart** — side-by-side visualization proving same engine gives completely different outputs for different profiles
- **TF-IDF heatmap** — shows which skills are most distinctive per role learned from real data (darker = more role-specific)
- **Role distribution chart** — EDA visualization showing candidate count per job role from the dataset
- **Vocabulary rule enforced** — underscores for multi-word skills (`machine_learning` not `machine learning`) to prevent vocabulary mismatch failures

### 🗂️ Dataset
```
File    : candidate_job_role_dataset.csv
Records : 1000 real candidates
Columns : candidate_id | skills | qualification | experience_level | job_role
Roles   : 20+ unique job titles
Skills  : Extracted automatically via TF-IDF vocabulary

Sample Roles:
  Data Scientist, AIML Engineer, Frontend Developer,
  Backend Developer, DevOps Engineer, Blockchain Developer,
  Cybersecurity Engineer, Mobile Developer, Data Analyst,
  Kubernetes Operations Engineer, Game Developer...

Sample Skills Vocabulary (auto-extracted):
  python, sql, machine_learning, tensorflow, deep_learning,
  javascript, react, html, css, node.js, docker, kubernetes,
  aws, linux, java, kotlin, swift, ios_development,
  penetration_testing, solidity, ethereum, blockchain,
  agile, scrum, figma, ui/ux_design, nlp, data_analysis...
```

### 🎯 Sample Output
```
  Input Skills: Python, Machine Learning, SQL, TensorFlow, NLP

  #1  Data Scientist     → 89.2% match  (50 real candidates)
  #2  AIML               → 81.4% match  (45 real candidates)
  #3  Data Analyst       → 64.3% match  (48 real candidates)
  #4  Full Stack Python  → 51.7% match  (47 real candidates)
  #5  Backend Developer  → 38.2% match  (50 real candidates)

  ── Skill Gap: Data Scientist (from real candidate data) ────
  ✅ You Have  : python, sql, machine_learning,
                 tensorflow, nlp
  ❌ To Learn  : pandas, statistics, data_visualization,
                 deep_learning, keras, r
  💡 Bonus     : nlp (adds value beyond base requirements)
  Coverage: 45.0% → 55.0% gap to close
  ───────────────────────────────────────────────────────────
```

### 📦 Tech Stack
```
Python   Scikit-learn (TfidfVectorizer + cosine_similarity)
Pandas   NumPy   Matplotlib   Seaborn   Google Colab
Dataset: candidate_job_role_dataset.csv
```


---

## 🧠 Skills Demonstrated Across All Projects

| Skill | P1 ARIA | P2 KNN | P3 Recommender |
|---|:---:|:---:|:---:|
| Python 3.14 | ✅ | ✅ | ✅ |
| IPO Architecture | ✅ | ✅ | ✅ |
| Modular Code Design | ✅ | | |
| O(1) Data Structures | ✅ | | |
| Input Sanitization | ✅ | | |
| File I/O & Audit Logging | ✅ | | |
| Session Statistics Tracking | ✅ | | |
| Exploratory Data Analysis | | ✅ | |
| Feature Scaling (StandardScaler) | | ✅ | |
| Train-Test Split (Stratified) | | ✅ | |
| Supervised Learning (KNN) | | ✅ | |
| Hyperparameter Tuning (Elbow) | | ✅ | |
| Confusion Matrix | | ✅ | |
| F1 Score Evaluation | | ✅ | |
| Model Comparison | | ✅ | |
| Live Predictor with Confidence | | ✅ | |
| TF-IDF Vectorization | | | ✅ |
| Cosine Similarity | | | ✅ |
| Content-Based Filtering | | | ✅ |
| 4-Step Ranking Pipeline | | | ✅ |
| Cold Start Handling | | | ✅ |
| Skill Gap Analysis | | | ✅ |
| Data Visualization (5+ charts) | | ✅ | ✅ |

---

## 📈 Project Progression

```
Project 1                Project 2                Project 3
─────────────────        ─────────────────        ──────────────────────
Rule-Based Logic    →    Supervised Learning  →   Recommendation Engine
─────────────────        ─────────────────        ──────────────────────
Deterministic            Probabilistic            Similarity-Based
O(1) Dictionary          KNN Algorithm            Cosine Similarity
No training data         Learns from data         TF-IDF Vectors
White Box / Explicit     Trained Model            Content-Based Filtering
Terminal App             Jupyter Notebook         Jupyter Notebook
VS Code                  Google Colab             Google Colab
```

---

## 👩‍🎓 About the Developer

**Kashaf**
AI Engineering Intern @ DecodeLabs | Final Year CS Student
Building: Synora — Federated Learning Toolkit for Low-Resource Languages

[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=flat-square&logo=github)](https://github.com)

---

## 🏢 About DecodeLabs

DecodeLabs is an AI-focused industrial training organization providing
hands-on project-based learning for the next generation of AI engineers.

🌐 www.decodelabs.tech
📍 Greater Lucknow, India

---

<div align="center">

**⭐ If this repository helped you, consider giving it a star!**

*Built with dedication during DecodeLabs AI Internship — Batch 2026*

</div>
```
