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
        print("DEBUG TYPE:", type(env.state))
print("DEBUG VALUE:", env.state)
print("DEBUG CALL TYPE:", type(env.state()))
print("DEBUG CALL VALUE:", repr(env.state()))

        # Just return it raw for now
        return {"state": repr(state)}

    except Exception as e:
        return {"error": f"State not initialized or invalid: {e}"} 

def main():
    return app
