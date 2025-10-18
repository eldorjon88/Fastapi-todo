from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    name: str = Field(max_length=128)
    description: str | None = Field(None)
    

class TaskOut(TaskCreate):
    id: int
    user_id: int
    status: bool







from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[int] = Field(3, ge=1, le=5)  # 1–5 oraliqda

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
