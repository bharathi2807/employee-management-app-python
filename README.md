
---

# 📄 1. README.md

````
# Employee Management REST API

A simple backend application built using FastAPI to manage employee records with CRUD operations.

## 🚀 Features
- Create employee
- Get all employees
- Get employee by ID
- Update employee
- Delete employee
- Input validation using Pydantic
- SQLite database integration

## 🛠 Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/employee-api.git
cd employee-api
````

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Open in browser

```
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| GET    | /employees      | Get all employees  |
| GET    | /employees/{id} | Get employee by ID |
| POST   | /employees      | Create employee    |
| PUT    | /employees/{id} | Update employee    |
| DELETE | /employees/{id} | Delete employee    |

## 📷 Sample Request

```json
{
  "name": "Bharathi",
  "role": "Developer",
  "salary": 50000
}
```

## 📷 Sample Response

```json
{
  "id": 1,
  "name": "Bharathi",
  "role": "Developer",
  "salary": 50000
}
```
