import json
import csv
import os

from models.customer import Customer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CUSTOMERS_FILE = os.path.join(BASE_DIR, "data", "customers.json")
CUSTOMERS_CSV = os.path.join(BASE_DIR, "data", "customers.csv")

def load_customers():
    with open(CUSTOMERS_FILE, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return [Customer.from_dict(item) for item in data] 
    
def save_customers(customers):
    with open(CUSTOMERS_FILE, 'w', encoding="utf-8") as f:
        json.dump([customer.to_dict() for customer in customers], f, ensure_ascii=False, indent=2)

def register_customers(customers):
    print("\n---Register Customer---")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()

    customer = Customer(name, email, phone)
    customers.append(customer)
    save_customers(customers)
    print("Customer Registered")
    print(customer)

def get_all_customers(customers):
    print("\n---Get Customer---")
    if not customers:
        print("No Customer located.")
        return
    for customer in customers:
        print(customer)

def get_customer_with_name_or_email(customers):
    print("\n---Get Customer---")
    value = input("Name or Email of the customer: ").strip().lower()
    results = [customer for customer in customers if value in customer.name.lower() or value in customer.email.lower()]
    if not results:
        print("No Customer Found.")
    else: 
        print(f"\n{len(results)} match(es)")
        for customer in results:
            print(customer)

def update_customers(customers):
    print("\n---Update Customer---")
    customer_id = input("ID of the Customer: ").strip().lower()
    result = [b for b in customers if customer_id in b.id]
    if not result:
        print("No customer located.")
        return
    
    customer = result[0]
    print(f"Current customer: {customer}")

    new_name = input(f"New name [{customer.name}]: ").strip()
    new_email = input(f"New email [{customer.email}]: ").strip()
    new_phone = input(f"New phone [{customer.phone}]: ").strip()
    

    if new_name:
        customer.name = new_name
    if new_email:
        customer.email = new_email
    if new_phone:
        customer.phone = new_phone

    save_customers(customers)
    print(f"Customer updated: {customer}")

def delete_customer(customers):
    print("\n---Delete Customer---")
    id = input("ID of the Customer: ").strip().lower()
    result = [customer for customer in customers if id in customer.id]
    if not result:
        print("No customer located.")
        return
    
    confirmation = input("Confirm if this is the correct customer to be deleted? Y/N").strip().lower()

    if confirmation == "y":
        customers.remove(result.next())
        save_customers(customers)
        print("Customer Deleted.")
    else:
        "Customer won't be deleted."

def export_customer_CSV(customers):
    if not customers:
        print("No Customer to Export.")
        return
    with open(CUSTOMERS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email", "Phone"])
        for customer in customers:
            writer.writerow([customer.id, customer.name, customer.email, customer.phone])
    print(f"Customers exported to CSV file: {CUSTOMERS_CSV}")