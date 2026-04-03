import os
import json
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# ---------- RULE BASED ----------
def rule_based_agent(obs):
    text = obs["email_text"].lower()

    if "refund" in text:
        return {"category": "support", "priority": "medium", "action": "reply", "response": "Refund will be processed"}

    if "delay" in text or "not arrived" in text:
        return {"category": "support", "priority": "high", "action": "escalate", "response": "We are escalating your issue"}

    if "offer" in text or "sale" in text:
        return {"category": "sales", "priority": "low", "action": "archive", "response": "Promotional email"}

    return {"category": "personal", "priority": "low", "action": "archive", "response": "Noted"}


# ---------- GEMINI ----------
def gemini_agent(obs):
    try:
        from google import genai

        client = genai.Client(api_key=API_KEY)

        prompt = f"""
You are an email triage AI.

STRICT RULES:
- Category MUST be one of: support, spam, sales, personal
- Priority MUST be: high, medium, low
- Action MUST be one of: reply, archive, ignore

Email:
Subject: {obs['subject']}
Body: {obs['email_text']}
Sender: {obs['sender']}

Return JSON ONLY:
{{
  "category": "...",
  "priority": "...",
  "action": "...",
  "response": "..."
}}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        print("\nGemini Raw Response:\n", text)

        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        print("❌Gemini Error:", e)
        time.sleep(2)
        return rule_based_agent(obs)