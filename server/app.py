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
        "subject": state["subject"] if state else "",
        "body": state["body"] if state else "",
        "reward": reward if isinstance(reward, float) else getattr(reward, "value", 0.0),
        "done": done
    }

@app.get("/state")
def get_state():
    try:
        state = env.state   # <-- no ()
        # If state is a dict with subject/body
        if isinstance(state, dict):
            return {
                "subject": state.get("subject", ""),
                "body": state.get("body", "")
            }
        # If state has "current_email"
        if isinstance(state, dict) and "current_email" in state:
            email = state["current_email"]
            return {
                "subject": email.get("subject", ""),
                "body": email.get("body", "")
            }
        # If state is a tuple/list
        if isinstance(state, (list, tuple)) and len(state) >= 2:
            return {
                "subject": state[0],
                "body": state[1]
            }
        return {"state": str(state)}
    except Exception as e:
        return {"error": f"State not initialized or invalid: {e}"}
    except:
        return {"error": "State not initialized"}

def main():
    return app
