from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    role: str
    salary: int

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True