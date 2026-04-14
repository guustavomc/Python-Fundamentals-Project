import json
import csv
import os

from models.book import Book


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

def register_book(books):
    print("\n---Register Book---")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    pages = int(input("Pages: ").strip())
    price = float(input("Price: ").strip())
    edition = int(input("Edition: ").strip())


    book = Book(title, author, pages)
    book.price = price
    book.edition = edition

    books.append(book)
    save_books(books)
    print("Book Registered")
    print(book)
    
