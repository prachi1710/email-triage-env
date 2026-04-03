from environment import EmailEnv
from rl_agent import rl_agent

env = EmailEnv()

def run_inference():
    obs = env.reset()

    # 🔥 Use trained RL agent
    action = rl_agent(obs, epsilon_override=0)

    obs, reward, done, _ = env.step(action)

    return {
        "observation": obs,
        "action": action,
        "reward": float(reward.score),
        "done": bool(done)
    }


if __name__ == "__main__":
    print(run_inference())