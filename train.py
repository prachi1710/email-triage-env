from environment import EmailEnv
from rl_agent import rl_agent, update_q, get_state, decay_epsilon, Q

env = EmailEnv()

episodes = 100

rewards = []

for ep in range(episodes):
    obs = env.reset()
    state = get_state(obs)

    action = rl_agent(obs)
    _, reward, _, _ = env.step(action)

    update_q(state, action, reward.score)
    decay_epsilon()

    rewards.append(reward.score)

    avg_reward = sum(rewards) / len(rewards)
    if (ep + 1) % 10 == 0:
        print("Current Q-table size:", len(Q))
    if (ep+1) % 20 == 0:
        print(f"🔥 Last 20 avg: {sum(rewards[-20:]) / 20:.2f}")

    print(f"Episode {ep+1} → Reward: {reward.score} | Avg: {avg_reward:.2f}")