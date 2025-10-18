from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    hashed_password: str

    class Config:
        from_attributes = True









from pydantic import BaseModel, EmailStr
from datetime import date
from enum import Enum
from typing import Optional


class UserRole(str, Enum):
    admin = "admin"
    user = "user"


class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = UserRole.user


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
