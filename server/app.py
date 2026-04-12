from fastapi import FastAPI
from env import EmailTriageEnv

app = FastAPI()

env = EmailTriageEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    print("DEBUG RESET STATE:", state)   # 👈 this shows what reset returns
    print("DEBUG ENV.STATE:", env.state) # 👈 this shows what env.state holds
    return {
        "subject": state["subject"],
        "body": state["body"]
    }
@app.post("/step")
def step(action: dict):
    action_str = action.get("action", "")

    state, reward, done, _ = env.step(action_str)

    return {
        "subject": state["subject"] if state else "",
        "body": state["body"] if state else "",
        "reward": reward if isinstance(reward, float) else getattr(reward, "value", 0.0),
        "done": done
    }
@app.get("/state")
def get_state():
    try:
        state = env.state()   # call the function

        # If it's a dict
        if isinstance(state, dict):
            return {
                "subject": state.get("subject") or state.get("current_email", {}).get("subject", ""),
                "body": state.get("body") or state.get("current_email", {}).get("body", "")
            }

        # If it's a tuple or list
        if isinstance(state, (list, tuple)) and len(state) >= 2:
            return {"subject": state[0], "body": state[1]}

        # If it's a custom object
        if hasattr(state, "subject") and hasattr(state, "body"):
            return {"subject": state.subject, "body": state.body}

        # Fallback
        return {"state": str(state)}

    except Exception as e:
        return {"error": f"State not initialized or invalid: {e}"}
def main():
    return app
