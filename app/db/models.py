# # from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey

# from app.db.database import Base


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(length=128), nullable=False, unique=True, index=True)
#     hashed_password = Column(String, nullable=False)
#     # add extra fields: first_name(required), last_name, birth_date, phone, email

#     # role: admin, user(default), oxirida

#     def __repr__(self) -> str:
#         return f'User(id={self.id}, username={self.username})'
    

# class Task(Base):
#     __tablename__ = 'tasks'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(length=128), nullable=False, index=True)
#     description = Column(Text, default='')
#     status = Column(Boolean, default=False, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     # add extra fields: category, priority(1-5)

#     def __repr__(self) -> str:
#         return f'Task(id={self.id}, name={self.name})'
    







from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.db.database import Base

# ------------------------------------------------------------
# USER ROLE ENUM
# ------------------------------------------------------------
class UserRole(PyEnum):
    admin = "admin"
    user = "user"

# ------------------------------------------------------------
# USER MODEL
# ------------------------------------------------------------
class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    birth_date = Column(Date)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.user)

    # relationship
    tasks = relationship("Task", back_populates="user")

# ------------------------------------------------------------
# TASK MODEL
# ------------------------------------------------------------
class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    priority = Column(Integer, default=3)
    user_id = Column(Integer, ForeignKey("users.id"))

    # relationship
    user = relationship("User", back_populates="tasks")
