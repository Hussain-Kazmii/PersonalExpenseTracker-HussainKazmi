"""
Penniflect
------------------------
A simple console program to help you track your daily expenses.

This program lets you:
    1. Add an expense
    2. View all expenses
    3. Search for an expense
    4. Delete an expense
    5. Calculate total spending
    6. See spending grouped by category
    7. Show the highest expense
    8. Save data to a file
    9. Exit the program

Data is stored as a list of dictionaries, and each dictionary looks like:
    {"date": "2026-07-27", "category": "Food", "description": "Lunch", "amount": 12.5}

The data is saved to (and loaded from) a JSON file called "expenses.json"
so your expenses are still there next time you run the program.
"""

# json is used to save/load our expenses list in a human-readable file format
import json

# os is used to check whether our data file already exists before loading it
import os

# The name of the file where we will store our expenses
DATA_FILE = "expenses.json"


def load_data():
    """
    Loads expenses from the JSON file (if it exists) when the program starts.
    Returns a list of expense dictionaries. If no file is found, returns an
    empty list so the program can still run normally.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        # "with" automatically closes the file for us once we're done reading
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        # This handles the case where the file is missing, empty, corrupted,
        # or can't be read for some other reason (e.g. permissions).
        print("Could not read saved data. Starting with an empty expense list.")
        return []


def save_data(expenses):
    """
    Saves the current list of expenses to the JSON file.
    "indent=4" just makes the file nicely formatted and easy to read.
    Wrapped in try/except so a file/permission problem never crashes the program.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(expenses, file, indent=4)
        print("\nData Saved Successfully.\n")
    except OSError as error:
        print(f"\nCould not save data ({error}). Your expenses are still safe in this session.\n")


def print_expense(expense, index=None):
    """
    Prints a single expense in a consistent format.
    This one function is reused by view_expenses(), search_expense(),
    and highest_expense() so the formatting logic only lives in one place
    (avoids repeating the same print statement three times).

    'index' is optional — pass it in when you want a serial number shown
    (e.g. for view_expenses), or leave it out otherwise.
    """
    prefix = f"{index}. " if index is not None else ""
    print(f"{prefix}Date: {expense['date']} | "
          f"Category: {expense['category']} | "
          f"Description: {expense['description']} | "
          f"Amount: {expense['amount']:.2f}")


def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Calculate Total Spending")
    print("6. Display Spending by Category")
    print("7. Show Highest Expense")
    print("8. Save Data")
    print("9. Exit")
    print("=====================================")


def add_expense(expenses):
    """
    Asks the user for the details of a new expense, stores it as a
    dictionary, and appends it to the expenses list.
    """
    date = input("Enter the date (e.g. 2026-07-27): ").strip()
    category = input("Enter the category (e.g. Food, Transport): ").strip()
    description = input("Enter a short description: ").strip()

    # We keep asking for the amount until the user enters a valid number
    while True:
        amount_input = input("Enter the amount spent: ").strip()
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Please enter a valid number for the amount.")

    # Store all the details together in one dictionary
    new_expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    # Add the new expense dictionary to our list of expenses
    expenses.append(new_expense)

    print("\nExpense Added Successfully.\n")


def view_expenses(expenses):
    """
    Displays every expense currently stored, along with its position
    number in the list (useful later for deleting a specific expense).
    """
    if len(expenses) == 0:
        print("\nNo expenses found.\n")
        return

    print("\n--- All Expenses ---")
    for index, expense in enumerate(expenses, start=1):
        print_expense(expense, index)
    print("--------------------\n")


def search_expense(expenses):
    """
    Asks the user for a keyword and searches through the category
    and description fields of every expense for a match.
    """
    if len(expenses) == 0:
        print("\nNo expenses found.\n")
        return

    keyword = input("Enter a category or keyword to search for: ").strip().lower()

    # We'll collect any matches we find in this list
    matches = []
    for expense in expenses:
        if keyword in expense["category"].lower() or keyword in expense["description"].lower():
            matches.append(expense)

    if len(matches) == 0:
        print(f"\nNo expenses found matching '{keyword}'.\n")
    else:
        print(f"\n--- Expenses matching '{keyword}' ---")
        for expense in matches:
            print_expense(expense)
        print("-------------------------------------\n")


def delete_expense(expenses):
    """
    Shows all expenses with a serial number, then asks the user which
    one to delete, and removes it from the list.
    """
    if len(expenses) == 0:
        print("\nNo expenses found.\n")
        return

    view_expenses(expenses)

    while True:
        choice = input("Enter the number of the expense to delete (or 0 to cancel): ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)
        if choice == 0:
            print("Delete cancelled.\n")
            return
        if 1 <= choice <= len(expenses):
            # Remove the expense at this position.
            # We subtract 1 because lists start counting from 0,
            # but we showed the expenses to the user starting from 1.
            removed = expenses.pop(choice - 1)
            print(f"\nDeleted expense: {removed['description']} "
                  f"({removed['amount']:.2f})\n")
            return
        else:
            print("That number doesn't match any expense. Try again.")


def calculate_total(expenses):
    """
    Adds up the amount of every expense and displays the total.
    """
    total = 0
    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: {total:.2f}\n")


def category_summary(expenses):
    """
    Groups expenses by category and displays the total spent in
    each category.
    """
    if len(expenses) == 0:
        print("\nNo expenses found.\n")
        return

    # This dictionary will store category names as keys,
    # and their running total as values.
    totals_by_category = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals_by_category:
            totals_by_category[category] += amount
        else:
            totals_by_category[category] = amount

    print("\n--- Spending by Category ---")
    for category, total in totals_by_category.items():
        print(f"{category}: {total:.2f}")
    print("-----------------------------\n")


def highest_expense(expenses):
    """
    Finds and displays the expense with the largest amount.
    """
    if len(expenses) == 0:
        print("\nNo expenses found.\n")
        return

    # Start by assuming the first expense is the highest
    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n--- Highest Expense ---")
    print_expense(highest)
    print("-----------------------\n")


def main():
    """
    Controls the overall program: loads existing data, shows the menu
    in a loop, and calls the correct function based on the user's choice.
    """
    # Load any previously saved expenses when the program starts
    expenses = load_data()

    # A dictionary that maps each menu number to the function that handles it.
    # This replaces a long if/elif chain: to add a new menu option later,
    # you just add one line here and write the matching function — nothing
    # else in main() needs to change, which makes the program easy to extend.
    menu_actions = {
        "1": add_expense,
        "2": view_expenses,
        "3": search_expense,
        "4": delete_expense,
        "5": calculate_total,
        "6": category_summary,
        "7": highest_expense,
        "8": save_data,
    }

    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-9): ").strip()

            if choice == "9":
                # Save data automatically before exiting so nothing is lost
                save_data(expenses)
                print("Thank you for using Personal Expense Tracker. Goodbye!")
                break
            elif choice in menu_actions:
                # Look up and call the right function for this choice
                menu_actions[choice](expenses)
            else:
                print("\nInvalid choice. Please enter a number between 1 and 9.\n")

        except (KeyboardInterrupt, EOFError):
            # Lets the user safely exit with Ctrl+C / Ctrl+D without a crash,
            # and still saves their data first.
            print("\n\nExiting early — saving your data first...")
            save_data(expenses)
            break
        except Exception as error:
            # A final safety net: if anything unexpected goes wrong, we show
            # a friendly message and return to the menu instead of crashing.
            print(f"\nSomething went wrong: {error}. Returning to the main menu.\n")


# This makes sure main() only runs when this file is executed directly,
# not if it's imported into another program.
if __name__ == "__main__":
    main()
