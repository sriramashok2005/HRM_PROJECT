from pydantic import BaseModel,Field

class Employeecreate(BaseModel):
    name: str
    age: int
    department: str
    email: str
    phone:str

class Employeeupdate(BaseModel):
    name: str | None = None 
    age: int | None = None
    department: str | None = None
    email: str | None = None
    phone:str | None = None

class UserCreate(BaseModel):
        username: str
        password: str= Field(min_length=8)

class Userlogin(BaseModel):
        username: str
        password: str= Field(min_length=8)  

class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    department: str
    email: str
    phone: str

class UserResponse(BaseModel):
    id: int
    username: str