---
title: Email Triage OpenEnv
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_file: run.py
pinned: false
---
# 📩 Email Triage OpenEnv Environment

## 🚀 Overview

This project implements a **real-world Email Triage System** as an **OpenEnv-compatible environment**, where an AI agent learns to classify and respond to emails using **Reinforcement Learning (RL)**.

The system simulates tasks that humans perform daily:
- Categorizing emails (support, spam, sales, personal)
- Assigning priority (low, medium, high)
- Deciding actions (reply, archive, ignore)
- Generating appropriate responses

---

## 🎯 Objective

Build an intelligent agent that:
- Understands incoming emails
- Takes correct actions
- Learns from rewards over time
- Improves performance using RL

---

## 🧠 Environment Design

### 📥 Observation Space (State)

```python
{
  "subject": str,
  "email_text": str,
  "sender": str,
  "task_type": str  # easy | medium | hard
}

🔹 Action Space

The agent must return:
```json
{
  "category": "support | spam | sales | personal",
  "priority": "high | medium | low",
  "action": "reply | archive | ignore",
  "response": "string"
}

🔹 Reward Function

Reward is calculated based on correctness:

✅ Category match → +0.4
✅ Priority match → +0.2
✅ Action match → +0.2
✅ Response quality → +0.2

Penalties:

❌ Empty response → -0.1
❌ Invalid category → -0.1

Final score: 0.0 → 1.0

OpenEnv API
reset()
Loads a new email sample
Returns initial observation

step(action)
Evaluates agent action
Returns:

observation, reward, done, info

state()
Returns current environment state

Task Design

The environment includes 3 difficulty levels:

🟢 Easy
Clean, structured emails
Clear intent

Example:

"I want a refund for my order"

🟡 Medium
Slight ambiguity
Requires interpretation

Example:

"The product quality is not good"

🔴 Hard
Noisy, informal, incomplete
Requires reasoning

Example:

"hey ordered last wk… no update 😕"

📈 Difficulty Progression

The environment increases complexity by introducing:

Typos and slang
Missing context
Ambiguous intent

Grader Design

The grader evaluates agent performance using:

Component	Weight
Category	0.3
Priority	0.2
Action	    0.2
Response	0.3

Features:
Handles synonyms and variations
Provides partial scores
Fully deterministic

🤖 Agents
1. Gemini Agent
Uses Gemini API
Generates structured output

2. Rule-Based Agent
Simple keyword-based logic
Used as baseline

3. RL Agent (Q-Learning Inspired)
Learns from rewards
Stores state-action pairs
Improves over time via experience

Reinforcement Learning Loop

for episode in range(N):
    state = env.reset()
    action = agent(state)
    _, reward, _, _ = env.step(action)
    update_q(state, action, reward)

📊 Baseline Results
Agent	    Average Score
Gemini	    ~0.6–0.8
Rule-based	~0.4–0.6
RL Agent    ~0.45-0.6

⚙️ Setup Instructions
1. Clone repository
git clone <your-repo>
cd email-triage-env

2. Install dependencies
pip install -r requirements.txt
3. Set API Key

Create .env file:

GEMINI_API_KEY=your_api_key_here

4. Run environment
python run.py

🐳 Docker Setup
Build image
docker build -t email-env .
Run container
docker run email-env

🤗 Hugging Face Deployment
Create a new Space
Select Docker template
Upload all project files
Add environment variable:
GEMINI_API_KEY

Deploy 🚀
📁 Project Structure
Email-Triage/
│
├── environment.py
├── data.py
├── agents.py
├── rl_agent.py
├── train.py
├── run.py
├── openenv.yaml
├── Dockerfile
└── README.md

Run locally
python run.py

Train RL agent
python train.py

## 🔐 API Key Setup

This project uses Gemini API for advanced email understanding.

Set your API key as an environment variable:

### Local
export GEMINI_API_KEY=your_api_key

### Docker
docker run -e GEMINI_API_KEY=your_api_key email-env

### Hugging Face Spaces
Add GEMINI_API_KEY in Space → Settings → Secrets

If no API key is provided, the system automatically falls back to a rule-based agent.

🏆 Key Features

✅Real-world task simulation
✅ OpenEnv compliant design
✅ Reinforcement learning integration
✅ Multi-agent comparison
✅ Robust to API failures
✅ Containerized deployment

🔥 Future Improvements
Use Deep Q-Learning instead of simple Q-table
Add memory/context across emails
Fine-tune LLM for domain-specific tasks
Improve reward shaping

📌 Conclusion

This project demonstrates how AI agents can:

Learn from interaction
Adapt to real-world scenarios
Improve decision-making over time

It bridges LLMs + RL + Environment Design, making it a strong foundation for intelligent automation systems.