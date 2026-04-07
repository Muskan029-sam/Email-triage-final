import gradio as gr
from env import EmailTriageEnv
from baseline_agent import RuleBasedAgent

def run_demo():
    env = EmailTriageEnv()
    agent = RuleBasedAgent()

    email = env.reset()
    output = ""

    while email is not None:
        action = agent.act(email["subject"])

        email, reward, done, _ = env.step(action)

        output += f"📩 Email: {email}\n"
        output += f"🤖 Action: {action}\n"
        output += f"⭐ Reward: {reward}\n\n"

        if done:
            break

    return output


iface = gr.Interface(
    fn=run_demo,
    inputs=[],
    outputs="text",
    title="📧 Email Triage AI",
    description="Classifies emails into spam, priority, or reply"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
