from sqlalchemy import Column, Integer, String
from app.database import BASE

class Employee(BASE):
    __tablename__ = "employees"
    
    name = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer,nullable=False)
    department = Column(String,nullable=False)
    email = Column(String, unique=True, index=True,nullable=False)  
    phone = Column(String, nullable=False)

class User(BASE):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
