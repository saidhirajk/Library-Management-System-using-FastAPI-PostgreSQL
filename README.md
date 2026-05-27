# 📚 Library Management System using FastAPI & PostgreSQL

A backend-only Library Management System built using FastAPI and PostgreSQL that performs CRUD operations on books.

This project demonstrates how to build REST APIs using FastAPI and connect them with a PostgreSQL database using psycopg2.

---

# 🚀 Features

✅ Add a new book  
✅ View all books  
✅ View a single book by ID  
✅ Update a book  
✅ Partially update a book  
✅ Delete a book  
✅ PostgreSQL database integration  
✅ Interactive Swagger UI documentation  

---

# 🛠️ Technologies Used

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Pydantic
- Uvicorn

---

# 📂 Project Structure

```bash
Library-Management-System/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Library-Management-System-using-FastAPI-PostgreSQL.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Library-Management-System-using-FastAPI-PostgreSQL
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🐘 PostgreSQL Database Setup

## Create Database

```sql
CREATE DATABASE library_db;
```

---

## Create Table

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_year INT NOT NULL
);
```

---

# ▶️ Run the Application

```bash
uvicorn main:app --reload
```

---

# 🌐 API Documentation

After running the server, open:

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home Route |
| GET | `/books` | Get All Books |
| GET | `/books/{id}` | Get Single Book |
| POST | `/books` | Add New Book |
| PUT | `/books/{id}` | Update Full Book |
| PATCH | `/books/{id}` | Partial Update |
| DELETE | `/books/{id}` | Delete Book |

---

# 📥 Sample JSON for POST Request

```json
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "published_year": 2018
}
```

---

# 🧠 Concepts Used

- REST API Development
- CRUD Operations
- Path Parameters
- Request Body Validation
- Pydantic Models
- PostgreSQL Queries
- Database Connectivity
- FastAPI Routing

---

# 📸 Database Verification

The database operations were successfully verified using PostgreSQL and pgAdmin on the local system.

Since PostgreSQL databases run locally on the machine, the actual database files and live data are not included in this GitHub repository. However, all SQL table creation commands and API functionality are provided in the project.

---

# 📦 requirements.txt

```txt
fastapi
uvicorn
psycopg2-binary
pydantic
```

---

# 👨‍💻 Author

Saidhiraj Kadwajiwar

---

# ⭐ Future Improvements

- JWT Authentication
- Docker Support
- Search Functionality
- Pagination
- Database ORM Integration
- Frontend UI

---

# 📄 License

This project is created for educational and learning purposes.
