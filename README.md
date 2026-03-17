

---
# Employee Management REST API

A backend application built using FastAPI to manage employee records with secure, scalable RESTful APIs. This project demonstrates API development, database integration, authentication, and modular backend architecture.

---

## 🚀 Features

- CRUD operations for employee management
- RESTful API design using FastAPI
- JWT-based authentication for secure endpoints
- Input validation using Pydantic
- Database integration using SQLAlchemy ORM
- API documentation using Swagger (OpenAPI)
- Modular project structure (routers, models, schemas)

---

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication (python-jose)
- Passlib (password hashing)

---

## 🔐 Authentication Flow

1. User logs in via `/login`
2. Server validates credentials and returns JWT token
3. Token must be passed in request header:
```

Authorization: Bearer <token>

````
4. Protected endpoints validate token before processing request

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/bharathi2807/employee-management-app-python.git
cd Employee
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Access API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description        |
| ------ | -------- | ------------------ |
| POST   | /login   | Generate JWT token |

### 👨‍💼 Employee APIs

| Method | Endpoint        | Description        | Protected |
| ------ | --------------- | ------------------ | --------- |
| GET    | /employees      | Get all employees  | ✅ Yes     |
| POST   | /employees      | Create employee    | ✅ Yes     |
| GET    | /employees/{id} | Get employee by ID | ❌ No      |
| PUT    | /employees/{id} | Update employee    | ❌ No      |
| DELETE | /employees/{id} | Delete employee    | ❌ No      |

---

## 📷 Sample Login Request

```json
{
  "username": "admin",
  "password": "admin123"
}
```

## 📷 Sample Login Response

```json
{
  "access_token": "your_token_here",
  "token_type": "bearer"
}
```

---

## 📷 Sample Employee Request

```json
{
  "name": "Bharathi",
  "role": "Developer",
  "salary": 50000
}
```

---

## 📷 Project Structure

```
.
├── main.py
├── models.py
├── schemas.py
├── database.py
├── auth.py
└── requirements.txt
```

---

## 🎯 Key Learnings

* Built REST APIs using FastAPI
* Implemented JWT-based authentication
* Used dependency injection for securing routes
* Integrated database using SQLAlchemy ORM
* Structured backend using modular architecture

---
