import json
import csv
import os

from app.models import book


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BOOKS_FILE = os.path.join(BASE_DIR, "data", "books.json")
BOOKS_CSV = os.path.join(BASE_DIR, "data", "books.csv")

def load_books():
    with open(BOOKS_FILE, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return [book.from_dict(item) for item in data] 
    
def save_books(books):
    with open(BOOKS_FILE, 'w', encoding="utf-8") as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=2)