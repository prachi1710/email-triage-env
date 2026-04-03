from environment import EmailEnv
from agents import rule_based_agent, gemini_agent
from rl_agent import rl_agent, update_q, get_state, decay_epsilon, Q
import time
import os

USE_GEMINI = True
API_KEY = os.getenv("GEMINI_API_KEY")


# ---------- SAFE GEMINI ----------
def safe_gemini(obs):
    if not USE_GEMINI:
        return rule_based_agent(obs)

    for attempt in range(2):
        try:
            return gemini_agent(obs)
        except Exception as e:
            print(f"⚠️ Gemini attempt {attempt+1} failed:", e)
            time.sleep(5)

    print("❌ Gemini failed → Falling back to Rule-based")
    return rule_based_agent(obs)


# =====================================================
# 🔥 MAIN EXECUTION (IMPORTANT FIX)
# =====================================================
if __name__ == "__main__":

    env = EmailEnv()

    # ---------------- RL TRAINING ----------------
    print("\n========== RL TRAINING ==========")

    episodes = 50
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
            print(f"Episode {ep+1} → Reward: {reward.score} | Avg: {avg_reward:.2f}")
            print("Q-table size:", len(Q))

    # ---------------- SINGLE RUN ----------------
    print("\n========== SINGLE RUN (POST-TRAINING) ==========")

    obs = env.reset()
    print("\n📩 Raw Input:", obs)

    action_rl = rl_agent(obs, epsilon_override=0)
    _, reward_rl, _, _ = env.step(action_rl)

    env.reset()
    action_r = rule_based_agent(obs)
    _, reward_r, _, _ = env.step(action_r)

    env.reset()
    action_g = safe_gemini(obs)
    _, reward_g, _, _ = env.step(action_g)

    print("\n--- Outputs ---")

    print("\n🧠 RL Output:", action_rl)
    print("RL Score:", reward_rl.score)

    print("\n📏 Rule-based Output:", action_r)
    print("Rule-based Score:", reward_r.score)

    print("\n🤖 Gemini Output:", action_g)
    print("Gemini Score:", reward_g.score)

    # ---------------- MULTI RUN ----------------
    print("\n========== AVERAGE PERFORMANCE ==========")

    runs = 3

    total_rl = 0
    total_r = 0
    total_g = 0

    for i in range(runs):
        print(f"\n--- Run {i+1} ---")

        obs = env.reset()
        print("📩 Raw Input:", obs)

        action_rl = rl_agent(obs, epsilon_override=0)
        _, reward_rl, _, _ = env.step(action_rl)

        env.reset()
        action_r = rule_based_agent(obs)
        _, reward_r, _, _ = env.step(action_r)

        env.reset()
        action_g = safe_gemini(obs)
        _, reward_g, _, _ = env.step(action_g)

        print("\n🧠 RL Output:", action_rl)
        print("RL Score:", reward_rl.score)

        print("\n📏 Rule-based Output:", action_r)
        print("Rule-based Score:", reward_r.score)

        print("\n🤖 Gemini Output:", action_g)
        print("Gemini Score:", reward_g.score)

        total_rl += reward_rl.score
        total_r += reward_r.score
        total_g += reward_g.score

    # ---------------- FINAL ----------------
    print("\n========== FINAL SCORES ==========")

    print("Average RL Score:", round(total_rl / runs, 2))
    print("Average Rule-based Score:", round(total_r / runs, 2))
    print("Average Gemini Score:", round(total_g / runs, 2))

    print("\n✅ Execution complete. Keeping container alive for demo...")
    time.sleep(10)
    while True:
        time.sleep(60)