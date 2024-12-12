from sqlalchemy import Column, Date, Integer, String, Boolean
from .database import Base  #Bass 重main改到database，所以要把main改到database



#Define Model

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    description = Column(String,nullable=True)
    completed = Column(Boolean,default=False)
    due_date = Column(Date, nullable=True)
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String(100),nullable=False)
    password = Column(String(100),nullable=False)
    email = Column(String(100),nullable=False)