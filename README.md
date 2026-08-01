<div align="center">

# 🤖 DecodeLabs AI Internship Projects
### Batch 2026 | Industrial Training Kit

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/DecodeLabs-AI%20Internship-purple?style=for-the-badge)

<br/>

> *"Before you build systems that learn on their own, you must master the art of  
> teaching a machine through explicit logic — and then let the data speak."*  
> — DecodeLabs, Batch 2026

</div>

---

## 👩‍💻 About This Repository

This repository documents my complete AI Engineering journey at **DecodeLabs** as part of the **Batch 2026 Industrial Training Kit**. It contains three progressive projects that build on each other — starting from deterministic rule-based logic, advancing to supervised machine learning, and culminating in a real-world recommendation engine.

Each project follows the **IPO (Input → Process → Output) architectural framework** and is built to professional standards — modular code, proper documentation, reproducible results, and presentation-ready outputs.

---

## 🗂️ Repository Structure

```
DecodeLabs-AI-Internship/
│
├── Project_1_Rule_Based_Chatbot/
│   ├── chatbot.py              ← Main entry point (run this)
│   ├── knowledge_base.py       ← All intents and responses
│   ├── utils.py                ← Colors, display, formatting
│   ├── logger.py               ← Session logging to file
│   ├── requirements.txt        ← Dependencies
│   └── chat_logs/              ← Auto-generated session logs
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

</div>

### 🎯 Goal
Build a terminal-based conversational AI agent that responds to user inputs using deterministic rule-based logic — the same control layer architecture used in production AI guardrail systems like NVIDIA NeMo and Llama Guard.

### 🏗️ Architecture
```
INPUT  →  Sanitization & Normalization
           ↓
PROCESS → 3-Tier Intent Matching Engine
           Tier 1: Exact Match    (O(1) Dictionary Lookup)
           Tier 2: Keyword Match  (Partial Scan)
           Tier 3: Fallback       (Random Response Pool)
           ↓
OUTPUT →  Color-Coded Response + Session Logging
```

### ✅ Key Requirements Met
| Requirement | Implementation |
|---|---|
| Handle greetings & exit commands | 40+ exact match intents + EXIT_COMMANDS set |
| Use if-else logic for responses | O(1) dictionary `.get()` — NOT if-elif ladder |
| Run in a continuous loop | `while True` heartbeat with graceful kill command |
| Input sanitization | `.lower().strip()` + punctuation removal |
| Fallback for unknowns | Random response pool via `random.choice()` |

### 🔑 Professional Features
- **Modular architecture** — 4 separate files, each with one responsibility
- **O(1) lookup** — Python dictionary instead of O(n) if-elif chain
- **Session logging** — every exchange saved to timestamped `.txt` file with match type labels
- **Color-coded terminal** — Cyan for matches, Red for fallbacks, Yellow for system messages
- **Session statistics** — total messages, exact/keyword/fallback counts, duration on exit
- **Graceful Ctrl+C handling** — no crash, clean shutdown

### 📦 Tech Stack
```
Python 3.14   Colorama   datetime   random   os
```

### ▶️ How to Run
```bash
# Install dependencies
pip install colorama

# Run the chatbot
python chatbot.py
```

### 🖥️ Sample Output
```
  🤖 ARIA ▸  Hello! I'm ARIA — your Rule-Based AI Assistant.

  You ▸  what is machine learning
  🤖 ARIA ▸  ML is a subset of AI where systems learn from data...
  ⚙  [Match: EXACT]
  ────────────────────────────────────────────────

  SESSION SUMMARY
  Total Messages Sent   :  14
  Matched (Exact)       :  8
  Matched (Keyword)     :  2
  Unmatched (Fallback)  :  0
  Session Duration      :  8m 12s
```

---

## 📁 Project 2 — Data Classification Using AI

<div align="center">

![Project2](https://img.shields.io/badge/Type-Supervised%20Learning-orange?style=flat-square)
![Tool](https://img.shields.io/badge/Tool-Google%20Colab-F9AB00?style=flat-square&logo=google-colab)
![Algorithm](https://img.shields.io/badge/Algorithm-KNN-green?style=flat-square)

</div>

### 🎯 Goal
Build a complete supervised machine learning pipeline that trains, evaluates, and deploys a KNN classifier on the Iris benchmark dataset — demonstrating the full journey from raw data to live predictions.

### 🏗️ Architecture
```
INPUT   →  Iris Dataset (150 samples | 3 classes | 4 features)
            Feature Scaling via StandardScaler (Mean=0, Var=1)
            80/20 Train-Test Split with Stratification
            ↓
PROCESS →  Elbow Method (K=1 to K=20) → Optimal K Selection
            KNN Classifier Training
            ↓
OUTPUT  →  Confusion Matrix | F1 Score | Classification Report
            Model Comparison (KNN vs Logistic Regression)
            Live Flower Species Predictor
```

### ✅ Key Requirements Met
| Requirement | Implementation |
|---|---|
| Load and understand dataset | Iris dataset with full EDA, pairplot, heatmap |
| Split into train/test sets | 80/20 stratified split with shuffle |
| Apply classification algorithm | KNN with Scikit-learn |
| Feature scaling | StandardScaler — fit on train, transform test only |
| Evaluation metrics | Confusion Matrix + F1 Score (not just accuracy) |

### 🔑 Professional Features
- **Elbow Method** — programmatically finds optimal K, no guessing
- **Data leakage prevention** — scaler fitted on training data only
- **F1 Score over accuracy** — avoids the "accuracy mirage" on imbalanced data
- **Model comparison** — KNN benchmarked against Logistic Regression
- **Live predictor** — enter any flower measurements, get species + confidence breakdown
- **Reproducibility** — `random_state=42` set everywhere

### 📊 Results
```
Optimal K Found   :  5
Model Accuracy    :  96.67%
F1 Score          :  96.67%
Confusion Matrix  :  Perfect diagonal (0 misclassifications on Setosa)
```

### 📦 Tech Stack
```
Python   Scikit-learn   Pandas   NumPy   Matplotlib   Seaborn
```

---

## 📁 Project 3 — AI Recommendation Logic

<div align="center">

![Project3](https://img.shields.io/badge/Type-Recommendation%20Engine-purple?style=flat-square)
![Tool](https://img.shields.io/badge/Tool-Google%20Colab-F9AB00?style=flat-square&logo=google-colab)
![Algorithm](https://img.shields.io/badge/Algorithm-Cosine%20Similarity-red?style=flat-square)

</div>

### 🎯 Goal
Build a **Tech Stack Recommender** — a content-based filtering engine that maps a user's skills to the most relevant tech career paths using TF-IDF vectorization and Cosine Similarity. The same core logic powering Netflix, Amazon, and Spotify recommendations.

### 🏗️ Architecture
```
INPUT   →  User Skills (min 3) → TF-IDF Vector
            Shared Vocabulary Space with Job Role Catalogue
            ↓
PROCESS →  4-Step Ranking Pipeline:
            Step 1: Ingestion  → Capture & vectorize user skills
            Step 2: Scoring    → Cosine Similarity vs all 15 roles
            Step 3: Sorting    → Rank by score descending
            Step 4: Filtering  → Return Top-N results only
            ↓
OUTPUT  →  Ranked Career Recommendations + Similarity Scores
            Skill Gap Analysis | Cold Start Fallback
```

### ✅ Key Requirements Met
| Requirement | Implementation |
|---|---|
| Take user input (min 3 skills) | Onboarding ingestion with vocabulary validation |
| Match using similarity logic | Cosine Similarity (NOT Euclidean — magnitude invariant) |
| Display recommended items | Top-N ranked list with scores, salary, descriptions |
| Content-based filtering | TF-IDF vectors on 15 job roles × 40+ unique skills |
| Cold start handling | Trending fallback when user provides no skills |

### 🔑 Professional Features
- **TF-IDF over binary** — penalizes generic skills, rewards specific ones
- **Cosine Similarity** — magnitude-invariant, industry standard for text matching
- **Skill Gap Analyzer** — shows matched skills, missing skills, coverage % per role
- **Cold Start Handler** — graceful fallback, no crash on empty input
- **Multi-user comparison** — side-by-side visualization of two skill profiles
- **"Why this recommendation?" explainer** — transparency in every suggestion
- **15 job roles catalogue** — Data Scientist, MLOps, DevOps, NLP Engineer, and more

### 🎯 Sample Output
```
  Input Skills: python, machine_learning, sql, tensorflow

  #1  Data Scientist          [Data & AI]      → 84.3% match
  #2  ML Engineer             [Data & AI]      → 79.1% match
  #3  AI Research Scientist   [Specialized AI] → 71.6% match
  #4  Data Engineer           [Data & AI]      → 58.2% match
  #5  MLOps Engineer          [Infrastructure] → 52.4% match

  Skill Gap — Data Scientist:
  ✅ Matched : python, sql, machine_learning, tensorflow
  ❌ To Learn: statistics, pandas, data_visualization
```

### 📦 Tech Stack
```
Python   Scikit-learn (TF-IDF + Cosine)   Pandas   NumPy
Matplotlib   Seaborn
```

---

## 🧠 Skills Demonstrated Across All Projects

| Skill | Project 1 | Project 2 | Project 3 |
|---|:---:|:---:|:---:|
| Python Programming | ✅ | ✅ | ✅ |
| IPO Architecture | ✅ | ✅ | ✅ |
| Data Structures (Dict/Set) | ✅ | | |
| Modular Code Design | ✅ | | |
| File I/O & Logging | ✅ | | |
| Data Exploration (EDA) | | ✅ | |
| Feature Scaling | | ✅ | |
| Supervised Learning | | ✅ | |
| Model Evaluation (F1, CM) | | ✅ | |
| Hyperparameter Tuning | | ✅ | |
| TF-IDF Vectorization | | | ✅ |
| Cosine Similarity | | | ✅ |
| Recommendation Systems | | | ✅ |
| Cold Start Handling | | | ✅ |
| Data Visualization | | ✅ | ✅ |

---

## 📈 Project Progression

```
Project 1          →      Project 2          →      Project 3
Rule-Based Logic          Supervised Learning        Recommendation Engine
─────────────────         ─────────────────          ─────────────────────
Deterministic             Probabilistic              Similarity-Based
O(1) Dictionary           KNN Algorithm              Cosine Similarity
No training data          Learns from data           Content-Based Filtering
White Box / Explicit      Black Box / Learned        Vector Space Matching
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
