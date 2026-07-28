"""
PERSONAL EXPENSE TRACKER - MVP VERSION
---------------------------------------
This is a stripped-down, minimum-viable version of the expense tracker.
It only includes the core features needed to make the program useful:

    1. Add an expense
    2. View all expenses
    3. Calculate total spending
    4. Exit (and save automatically)

Expenses are kept in memory as a list of dictionaries, and saved to a
JSON file called "expenses.json" so they aren't lost when you close
the program.
"""

import json  # used to save/load expenses to/from a file
import os     # used to check if the data file already exists

DATA_FILE = "expenses.json"


def load_data():
    """Loads expenses from file if it exists, otherwise starts with an empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_data(expenses):
    """Saves the expenses list to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Data saved.\n")


def add_expense(expenses):
    """Asks the user for expense details and adds them to the list."""
    date = input("Date: ").strip()
    category = input("Category: ").strip()
    description = input("Description: ").strip()

    # Keep asking until a valid number is entered, so the program never crashes here
    while True:
        try:
            amount = float(input("Amount: ").strip())
            break
        except ValueError:
            print("Please enter a valid number.")

    expenses.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    })
    print("Expense added.\n")


def view_expenses(expenses):
    """Displays all stored expenses."""
    if not expenses:
        print("No expenses found.\n")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['category']} | "
              f"{expense['description']} | {expense['amount']:.2f}")
    print()


def calculate_total(expenses):
    """Adds up and displays the total of all expenses."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spending: {total:.2f}\n")


def main():
    """Runs the main menu loop."""
    expenses = load_data()

    while True:
        # Show the menu
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            save_data(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
