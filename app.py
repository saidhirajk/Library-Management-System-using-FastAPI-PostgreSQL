import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Database Connection
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="########"
)

cursor = connection.cursor()


# -----------------------------
# Pydantic Models
# -----------------------------

class Book(BaseModel):
    title: str
    author: str
    published_year: int


class PatchBook(BaseModel):
    title: str = None
    author: str = None
    published_year: int = None
    
# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():
    return {"message": "Welcome to Library Management System API"}


# -----------------------------
# Get All Books
# -----------------------------

@app.get("/books")
def get_books():

    cursor.execute("SELECT * FROM books")

    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "published_year": row[3]
        })

    return result


# -----------------------------
# Get Single Book by ID
# -----------------------------

@app.get("/books/{id}")
def get_single_book(id: int):

    cursor.execute(
        "SELECT * FROM books WHERE id = %s",
        (id,)
    )

    row = cursor.fetchone()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "published_year": row[3]
        }

    return {"message": "Book not found"}


# -----------------------------
# Add New Book
# -----------------------------

@app.post("/books")
def add_book(book: Book):

    cursor.execute(
        """
        INSERT INTO books (title, author, published_year)
        VALUES (%s, %s, %s)
        """,
        (book.title, book.author, book.published_year)
    )

    connection.commit()

    return {"message": "Book added successfully"}


# -----------------------------
# Update Complete Book Record
# -----------------------------

@app.put("/books/{id}")
def update_book(id: int, book: Book):

    cursor.execute(
        """
        UPDATE books
        SET title = %s,
            author = %s,
            published_year = %s
        WHERE id = %s
        """,
        (book.title, book.author, book.published_year, id)
    )

    connection.commit()

    return {"message": f"Book with ID {id} updated successfully"}


# -----------------------------
# Partial Update
# -----------------------------

@app.patch("/books/{id}")
def partial_update_book(id: int, changes: PatchBook):

    if changes.title is not None:
        cursor.execute(
            "UPDATE books SET title = %s WHERE id = %s",
            (changes.title, id)
        )

    if changes.author is not None:
        cursor.execute(
            "UPDATE books SET author = %s WHERE id = %s",
            (changes.author, id)
        )

    if changes.published_year is not None:
        cursor.execute(
            "UPDATE books SET published_year = %s WHERE id = %s",
            (changes.published_year, id)
        )

    connection.commit()

    return {"message": f"Book with ID {id} updated successfully"}


# -----------------------------
# Delete Book
# -----------------------------

@app.delete("/books/{id}")
def delete_book(id: int):

    cursor.execute(
        "DELETE FROM books WHERE id = %s",
        (id,)
    )

    connection.commit()

    return {"message": f"Book with ID {id} deleted successfully"}