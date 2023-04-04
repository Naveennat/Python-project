from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    isbn: str
    title: str
    author: list
    price: float

books = {
    1:{
        "isbn": "b09bjlkm6f",
        "title": "Web API Development with Python",
        "author": ["Rehan Haider"],
        "price": 449.0
    },
    2:{
        "isbn": "9332585342",
        "title": "Python Programming - A modular approach",
        "author": ["Naveen"],
        "price": 599.0

    }
}
@app.get("/") #http:127.0.0.1:8000/
def home():
    return "hello world"

@app.get("/api/book/get_details")
def get_details():
    """Retrieve All Details from the book (R)
       Create - POST, Retrieve-GET, Update-PUT, Delete-DELETE
       Use: http://127.0.0.1:8000/docs URL for API Demo    
    """ 
    return books

@app.post("/api/book/create")
def create_book(new_book: Book):
    book_id = max(books.keys())+1
    books[book_id] = new_book.dict()
    return books

@app.put("/api/book/{book_id}")
def update_book(book_id: int, updated_book: Book):
    book = books[book_id]
    book["isbn"] = updated_book.isbn
    book["title"] = updated_book.title
    book["author"] = updated_book.author
    book["price"] = updated_book.price
    return books

@app.delete("/api/book/{book_id}")
def delete_book(book_id: int):
    del books[book_id]
    return books               

@app.delete("/api/book/")
def delete_books(book_ids: list):
    for book_id in book_ids:
        del books[book_id]
        return books
