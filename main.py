import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\nExpense History")
        print("-" * 50)

        for row in reader:
            print("{:<15} {:<15} {:<20} {}".format(*row))


def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            categories[category] = categories.get(category, 0) + amount

    print("\nCategory Summary")
    print("-" * 30)

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


initialize_file()
menu()
