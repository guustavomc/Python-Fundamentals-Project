import json
import csv
import os

from app.services.book_service import (load_books, register_book, 
                                       get_all_books, search_book_with_title_or_author, 
                                       update_book, delete_book, export_book_CSV)


from app.services.customer_service import (delete_customer, export_customer_CSV, 
                                           get_all_customers, get_customer_with_name_or_email, 
                                           load_customers, register_customers, update_customers)
from models.book import Book
from models.customer import Customer

def book_menu():
    books = load_books()
    while True:
        print("\n" + "=" * 40)
        print("         MANAGE BOOKS")
        print("=" * 40)
        print("1. Register Book")
        print("2. Get Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Export CSV")
        print("0. Back")
        print("-" * 40)
        opcao = input("Choose: ").strip()

        books = load_books()  # recarrega para garantir dados atualizados

        if opcao == "1":
            register_book(books)
        elif opcao == "2":
            get_all_books(books)
        elif opcao == "3":
            search_book_with_title_or_author(books)
        elif opcao == "4":
            update_book(books)
        elif opcao == "5":
            delete_book(books)
        elif opcao == "6":
            export_book_CSV(books)
        elif opcao == "0":
            break
        else:
            print("Invalid Option.")

def customer_menu():
    customers = load_customers()
    while True:
        print("\n" + "=" * 40)
        print("        GERENCIAR CLIENTES")
        print("=" * 40)
        print("1. Register Customer")
        print("2. Get Customers")
        print("3. Search Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Export CSV")
        print("0. Back")
        print("-" * 40)
        opcao = input("Choose: ").strip()

        customers = load_customers()

        if opcao == "1":
            register_customers(customers)
        elif opcao == "2":
            get_all_customers(customers)
        elif opcao == "3":
            get_customer_with_name_or_email(customers)
        elif opcao == "4":
            update_customers(customers)
        elif opcao == "5":
            delete_customer(customers)
        elif opcao == "6":
            export_customer_CSV(customers)
        elif opcao == "0":
            break
        else:
            print("Invalid Option.")


def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("       LIBRARY SYSTEM")
        print("=" * 40)
        print("1. Manage Books")
        print("2. Manage Customers")
        print("0. Quit")
        print("-" * 40)
        opcao = input("Choose: ").strip()

        if opcao == "1":
            book_menu()
        elif opcao == "2":
            customer_menu()
        elif opcao == "0":
            print("\nBye!")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    if login():
        menu_principal()