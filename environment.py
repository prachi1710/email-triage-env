from data import get_sample
from models import Observation, Reward
from data import get_email
from grader import grade
import random

class EmailEnv:

    def __init__(self):
        self.task_type = None
        self.email = None
        self.ground_truth = None

    def reset(self):
        self.current_email, self.ground_truth = get_sample()

        return {
            "subject": self.current_email["subject"],
            "email_text": self.current_email["email_text"],
            "sender": self.current_email["sender"],
            "task_type": self.current_email["task_type"]
        }

    def step(self, action):
        score = grade(action, self.ground_truth)

        # -------- Reward shaping --------
        reward_value = score

        # penalty for empty response
        if len(action.get("response", "")) < 5:
            reward_value -= 0.1

        # penalty for invalid category
        valid_categories = ["support", "spam", "sales", "personal"]
        if action.get("category", "").lower() not in valid_categories:
            reward_value -= 0.1

        # keep reward between 0 and 1
        reward_value = max(0.0, min(1.0, reward_value))

        reward = Reward(score=reward_value)
        done = True

        return self.current_email, reward, done, {}

    def state(self):
        return {
            "subject": self.current_email["subject"],
            "email_text": self.current_email["email_text"]
        }