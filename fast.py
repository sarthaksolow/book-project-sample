from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Setting up templates directory
templates = Jinja2Templates(directory="templates")

# Sample dataset (Books with genres)
books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help"},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "genre": "Self-help"},
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
]

# Homepage route with optional genre filtering
@app.get("/")
async def homepage(request: Request, genre: str = Query(None)):
    filtered_books = [book for book in books if book["genre"].lower() == genre.lower()] if genre else books
    genres = list(set(book["genre"] for book in books))  # Get unique genres
    return templates.TemplateResponse("index.html", {"request": request, "books": filtered_books, "genres": genres})
