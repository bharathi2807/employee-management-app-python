from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from pydantic import BaseModel

import models, schemas
from database import engine, SessionLocal
from auth import authenticate_user, create_access_token

# -------------------- CONFIG --------------------
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

# -------------------- APP INIT --------------------
app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# -------------------- DB DEPENDENCY --------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------- AUTH --------------------
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# -------------------- LOGIN --------------------
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})
    return {
        "access_token": token,
        "token_type": "bearer"
    }

# -------------------- EMPLOYEE APIs --------------------

# Create Employee (Protected)
@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(
    emp: schemas.EmployeeCreate,
    user=Depends(verify_token),
    db: Session = Depends(get_db)
):
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

# Get All Employees (Protected)
@app.get("/employees")
def get_employees(
    user=Depends(verify_token),
    db: Session = Depends(get_db)
):
    return db.query(models.Employee).all()

# Get Single Employee
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# Update Employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.name = updated.name
    emp.role = updated.role
    emp.salary = updated.salary

    db.commit()
    return {"message": "Employee updated"}

# Delete Employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}