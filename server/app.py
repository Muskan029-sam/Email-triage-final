from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailTriageEnv

app = FastAPI()
env = EmailTriageEnv()

# ✅ Typed request model for /step
class Action(BaseModel):
    action: str

@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "subject": state.get("subject", "") if isinstance(state, dict) else str(state),
        "body": state.get("body", "") if isinstance(state, dict) else ""
    }

@app.post("/step")
def step(action: Action):
    state, reward, done, _ = env.step(action.action)
    return {
        "subject": state.get("subject", "") if isinstance(state, dict) else str(state),
        "body": state.get("body", "") if isinstance(state, dict) else "",
        "reward": reward.value if hasattr(reward, "value") else reward,
        "done": done
    }

@app.get("/state")
def get_state():
    if not hasattr(env, "state") or env.state is None:
        return {"error": "State not initialized. Call /reset first."}
    
    state = env.state
    
    # If state is a dict
    if isinstance(state, dict):
        return {
            "subject": state.get("subject", ""),
            "body": state.get("body", "")
        }
    
    # If state is a tuple/list like (subject, body)
    if isinstance(state, (list, tuple)) and len(state) >= 2:
        return {
            "subject": state[0],
            "body": state[1]
        }
    
    # Fallback: just return string
    return {"state": str(state)}
