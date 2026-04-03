import random

Q = {}

categories = ["support", "spam", "sales", "personal"]
priorities = ["high", "medium", "low"]
actions_list = ["reply", "archive", "ignore"]

epsilon = 0.5  # start high
epsilon_min = 0.05
decay = 0.95


def get_state(obs):
    if obs is None:
        return "unknown"

    subject = obs.get("subject", "")
    task = obs.get("task_type", "unknown")

    return f"{task}_{subject.lower()[:20]}"

def get_random_action():
    return {
        "category": random.choice(["support", "spam", "sales", "personal"]),
        "priority": "medium",   # keep fixed initially
        "action": random.choice(["reply", "archive", "ignore"]),
        "response": "Auto-generated response"
    }

current_epsilon = 0.3
def rl_agent(obs, epsilon_override=None):
    state = get_state(obs)

    epsilon = epsilon_override if epsilon_override is not None else current_epsilon

    # Explore
    if random.random() < epsilon or state not in Q:
        return get_random_action()

    # Exploit (best action)
    best_action = max(Q[state], key=Q[state].get)
    return eval(best_action)


def update_q(state, action, reward, alpha=0.1):
    action_key = str(action)

    if state not in Q:
        Q[state] = {}

    if action_key not in Q[state]:
        Q[state][action_key] = 0.0

    # Q-learning update
    Q[state][action_key] += alpha * (reward - Q[state][action_key])


def decay_epsilon():
    global epsilon
    epsilon = max(epsilon_min, epsilon * decay)