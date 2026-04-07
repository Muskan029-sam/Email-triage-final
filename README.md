---
title: Email Triage Env
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_file: demo.py
pinned: false
---
# 📧 Email Triage Environment

[![OpenEnv Compliant](https://img.shields.io/badge/OpenEnv-Compliant-blue)](https://openenv.org)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-lightblue)](https://www.docker.com/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

---

## 📖 Overview

Email Triage Environment is a **real-world OpenEnv simulation** of how humans manage emails — filtering spam, prioritizing urgent messages, and responding appropriately.

This environment allows AI agents to **learn and be evaluated** on productivity workflows in a structured, reward-driven setting.

---

## 🎯 Tasks (Easy → Hard)

### 🟢 Task 1: Spam Detection (Easy)
- **Objective:** Identify spam emails
- **Action:** `spam_filter` or not
- **Reward:**  
  - Correct → `1.0`  
  - Incorrect → `0.0`

---

### 🟡 Task 2: Urgency Prioritization (Medium)
- **Objective:** Detect urgent emails
- **Actions:** `prioritize`, `reply`, `spam_filter`
- **Reward:**  
  - Correct → `1.0`  
  - Partially correct → `0.3`  
  - Incorrect → `0.0`

---

### 🔴 Task 3: Full Email Triage (Hard)
- **Objective:** Perform complete triage decision
- **Actions:**  
  - `spam_filter` (spam)  
  - `prioritize` (urgent)  
  - `reply` (normal)
- **Reward:**  
  - Correct → `1.0`  
  - Incorrect → `0.0`

---

## ⚙️ Environment Design

### 🔹 Observation Space
```json
{
  "subject": "string",
  "body": "string"
}

Action Space
Action
Description
spam_filter
Mark email as spam
prioritize
Mark as urgent
reply
Respond normally
🔹 RL Interface
obs = env.reset()

obs, reward, done, info = env.step(action)

reset() → initial email
step() → next state + reward
done → episode ends after inbox processed
🧠 Reward Design
Fully deterministic and reproducible
Score range: 0.0 → 1.0
Provides:
Correctness signal
Partial credit
Penalization of wrong actions

▶️ Quickstart
git clone https://github.com/<your-username>/email-triage-env.git
cd email-triage-env

pip install -r requirements.txt
python demo.py

🧪 Example Output

Step 1
Email Subject: Win a lottery!
Agent Action: spam_filter
Reward Received: 1.0
🤖 Baseline Agent
A rule-based agent is provided using keyword heuristics:
Detects spam via keywords like “win”, “lottery”
Detects urgency via “deadline”, “urgent”
📊 Baseline Scores
Task
Score
Spam Detection
1.0
Urgency Prioritization
0.8
Full Triage
0.9
Average
0.9
⚡ Inference Script
Run:
python inference.py
Output:
Final Score: 0.9

🐳 Docker Setup

docker build -t email-triage-env .
docker run -p 8000:8000 email-triage-env

python -m unittest discover tests

🌍 Real-World Use Case

This environment simulates real productivity workflows, useful for:
Email assistants
Customer support automation
Personal AI productivity tools

🚀 Future Improvements

LLM-based reply evaluation
Larger email datasets
Multi-user inbox simulation

🤝 Contributing
