from pydantic import BaseModel

class Observation(BaseModel):
    email_text: str
    subject: str
    sender: str
    task_type: str

class Action(BaseModel):
    category: str
    priority: str
    action: str
    response: str

class Reward(BaseModel):
    score: float