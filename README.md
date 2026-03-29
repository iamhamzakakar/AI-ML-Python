# Data Scientist / AI Engineer Track

This repository documents my **30-day structured journey** toward becoming a **Data Scientist / AI Engineer**, with a strong focus on **clean code, testing, MLOps, and real-world AI systems**.

The goal is not just to learn concepts, but to **implement them using industry-standard practices** and build a portfolio aligned with real engineering environments (e.g., banking, AI systems, and production ML).

---

## 🚀 Objectives

* Write **production-quality Python code**
* Apply **type safety and testing best practices**
* Build **machine learning pipelines and evaluation systems**
* Develop **LLM / GenAI applications (RAG, agents)**
* Learn **MLOps, deployment, and system design**
* Document progress and decisions like a real engineering project

---

## 🛠 Tech Stack

* **Python (typed, modular, production-style)**
* **pytest** → testing framework
* **mypy** → static type checking (`--strict`)
* **black** → code formatting
* **ruff** → linting and code quality
* **pre-commit** → automated code checks
* **pandas / NumPy** → data processing
* **scikit-learn** → ML pipelines
* **MLflow** → experiment tracking
* **FastAPI** → API development
* **Docker / Azure ML** → deployment (later stages)

---

## 📁 Project Structure

```
src/                        # Source code (production-style)
  my_python_project/
    __init__.py
    example.py
    refactored_functions.py

tests/                      # Test cases (pytest)
  test_example.py
  test_refactored_functions.py

pyproject.toml              # Project + tool configuration
.pre-commit-config.yaml     # Automated quality checks
README.md                   # Project documentation
```

---

## ⚙️ Development Workflow

All development follows a **production-style workflow**:

1. Write modular Python code inside `src/`

2. Add **type hints + docstrings (Google style)**

3. Write **pytest tests (happy path + edge cases)**

4. Run locally:

   ```bash
   pytest
   ```

5. Commit code:

   ```bash
   git add .
   git commit -m "clear message"
   ```

   → automatically runs:

   * black (formatting)
   * ruff (linting)
   * mypy (type checking)

6. Push to GitHub:

   ```bash
   git push
   ```

---

## 📊 Progress Tracker

### Week 1 — Python + ML Foundations

* [x] Day 1: Production Python & Code Quality
* [ ] Day 2: pandas & NumPy for Production
* [ ] Day 3: Scikit-learn Pipelines & Feature Engineering
* [ ] Day 4: Model Evaluation & Imbalanced Data
* [ ] Day 5: SQL & Database Querying for ML
* [ ] Day 6: Experiment Tracking with MLflow
* [ ] Day 7: Week 1 Integration Project

---

### Week 2 — LLMs & GenAI Engineering

* [ ] Day 8: LLM APIs & Prompt Engineering
* [ ] Day 9: Embeddings & Semantic Search
* [ ] Day 10: RAG Fundamentals
* [ ] Day 11: GenAI Evaluation & Quality
* [ ] Day 12: Fine-tuning & Prompt Optimization
* [ ] Day 13: LangChain & LangGraph Basics
* [ ] Day 14: Capstone — GenAI Investigation Assistant

---

### Week 3 — RAG & Agent Systems

* [ ] Day 15: Advanced RAG (HyDE, Reranking, Hybrid Search)
* [ ] Day 16: LangGraph Agents & Tool Use
* [ ] Day 17: Multi-Agent Systems
* [ ] Day 18: FastAPI (Production APIs)
* [ ] Day 19: Docker & Containerization
* [ ] Day 20: Azure ML & Cloud Deployment
* [ ] Day 21: Capstone — Deployed Investigation Agent

---

### Week 4 — MLOps, Azure & FinCrime AI

* [ ] Day 22: CI/CD for ML
* [ ] Day 23: Model Monitoring & Data Drift
* [ ] Day 24: Responsible AI & Explainability
* [ ] Day 25: Financial Crime AI (domain knowledge)
* [ ] Day 26: System Design for ML Applications
* [ ] Day 27: Stakeholder Communication & Writing
* [ ] Day 28: Interview Preparation
* [ ] Day 29: Final Capstone — Production GenAI System
* [ ] Day 30: Application Day

---

## 🧪 Implementations (Ongoing)

* Structured Python project using **src/ layout**
* Added **type-safe utility functions**
* Implemented **pytest tests with parametrization**
* Configured **pre-commit hooks (black, ruff, mypy)**
* Enforced **clean code + reproducible workflow**

---

## 📌 Key Learnings (Updated Regularly)

* Writing **type-safe Python** improves reliability and maintainability
* Automated tools (**black, ruff, mypy**) enforce consistent quality
* Testing with pytest ensures correctness and confidence
* Clean structure (`src/`, modular design) is critical for scaling projects

---

## 🔮 Next Steps

* Build **data pipelines using pandas & NumPy**
* Implement **ML pipelines with scikit-learn**
* Add **experiment tracking (MLflow)**
* Develop **LLM + RAG-based systems**
* Deploy models using **FastAPI + Docker + Azure**

---

## 📈 Philosophy

This repository focuses on:

> **"Learning by building production-quality systems — not just notebooks."**

Every component is written with:

* clarity
* correctness
* scalability
* real-world applicability

---

## 🤝 Author

This project is part of my focused effort to transition into a **Data Scientist / AI Engineer role**, with emphasis on **production ML systems and applied AI engineering**.

---
