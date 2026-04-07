# models.py
from pydantic import BaseModel
from typing import Any, Dict

class Observation(BaseModel):
    subject: str
    body: str

class Action(BaseModel):
    action_type: str  # e.g., "spam_filter", "prioritize", "reply"

class Reward(BaseModel):
    value: float
    info: Dict[str, Any] = {}
