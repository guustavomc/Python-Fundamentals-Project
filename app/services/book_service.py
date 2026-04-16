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
        return [Book.from_dict(item) for item in data] 
    
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

def get_all_books(books):
    print("\n---Get Book---")
    if not books:
        print("No Book located.")
        return
    for book in books:
        print(book)

    
def search_book_with_title_or_author(books):
    print("\n---Get Book With Title or Author---")
    value = input("Title or author of the Book: ").strip().lower()
    results = [b for b in books if value in b.title.lower() or value in b.author.lower()]
    if not results:
        print("No book located.")
    else:
        print(f"\n{len(results)} match(es)")
        for book in results:
            print(book)

def update_book(books):
    print("\n---Update Book---")
    book_id = input("ID of the Book: ").strip().lower()
    result = [b for b in books if book_id in b.id]
    if not result:
        print("No book located.")
        return
    
    print(f"Current book: {result[0]}")

    new_title = input(f"New title [{result.title}]: ").strip()
    new_author = input(f"New Author [{result.author}]: ").strip()
    new_pages = input(f"New pages [{result.pages}]: ").strip()
    new_price = input(f"New price [{result.price:.2f}]: ").strip()
    new_edition = input(f"New edition [{result.edition}]: ").strip()

    if new_title:
        result.title = new_title
    if new_author:
        result.author = new_author
    if new_pages:
        result.pages = int(new_pages)
    if new_price:
        result.price = float(new_price)
    if new_edition:
        result.edition = int(new_edition)

    save_books(books)
    print(f"Book updated: {result}")

def delete_book(books):
    print("\n---Delete Book---")
    book_id = input("ID of the Book: ").strip().lower()
    result = [b for b in books if book_id in b.id]
    if not result:
        print("No book located.")
        return
    
    confirmation = input("Confirm if this is the correct book to be deleted? Y/N").strip().lower()

    if confirmation == "y":
        books.remove(result[0])
        save_books(books)
        print("Book Deleted.")
    else:
        "Book won't be deleted."

def export_book_CSV(books):
    if not books:
        print("No Book to Export.")
        return
    with open(BOOKS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Author", "Pages", "Edition", "Prices"])
        for book in books:
            writer.writerow([book.id, book.title, book.author, book.pages, book.price, f"{book.price:.2f}"])
    print(f"Books exported to CSV file: {BOOKS_CSV}")