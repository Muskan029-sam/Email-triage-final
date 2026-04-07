
from fastapi import FastAPI
from env import EmailTriageEnv

app = FastAPI()

env = EmailTriageEnv()


@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "subject": state["subject"],
        "body": state["body"]
    }


@app.post("/step")
def step(action: dict):
    action_str = action.get("action", "")

    state, reward, done, _ = env.step(action_str)

    return {
        "subject": state["subject"],
        "body": state["body"],
        "reward": reward.value if hasattr(reward, "value") else reward,
        "done": done
    }


@app.get("/state")
def get_state():
    # ✅ FIX: handle empty/uninitialized state safely
    if not hasattr(env, "state") or env.state is None:
        return {"error": "State not initialized. Call /reset first."}

    state = env.state

    return {
        "subject": state.get("subject", ""),
        "body": state.get("body", "")
    }


def main():
    return app

