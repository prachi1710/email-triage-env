from environment import EmailEnv
from rl_agent import rl_agent, update_q, get_state, decay_epsilon

env = EmailEnv()

def evaluate(agent_func, runs=20):
    total = 0

    for _ in range(runs):
        obs = env.reset()
        action = agent_func(obs)
        _, reward, _, _ = env.step(action)
        total += reward.score

    return total / runs


# -------- BEFORE TRAINING --------
print("\n========== BEFORE TRAINING ==========")

before_score = evaluate(lambda obs: rl_agent(obs, epsilon_override=0))
print("Avg RL Score (Before):", round(before_score, 2))


# -------- TRAINING --------
print("\n========== TRAINING ==========")

episodes = 100

for ep in range(episodes):
    obs = env.reset()
    state = get_state(obs)

    action = rl_agent(obs)
    _, reward, _, _ = env.step(action)

    update_q(state, action, reward.score)
    decay_epsilon()


# -------- AFTER TRAINING --------
print("\n========== AFTER TRAINING ==========")

after_score = evaluate(lambda obs: rl_agent(obs, epsilon_override=0))
print("Avg RL Score (After):", round(after_score, 2))