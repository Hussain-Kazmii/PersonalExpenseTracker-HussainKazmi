# Penniflect

Penniflect is a lightweight personal expense tracker built as a Python console application. It helps you record, organize, and reflect on your everyday spending — one entry at a time.

## 🌱 Why Penniflect?

"Penniflect" combines *penny* and *reflect* — the idea of pausing to reflect on where every penny goes. Most people lose track of daily spending simply because there's no easy place to log it. Penniflect gives you a simple, no-frills way to record expenses as they happen and look back on your habits whenever you want.

## ✨ Features

* Add expenses with date, category, description, and amount
* View every recorded expense in a clean, numbered list
* Search expenses by category or keyword
* Delete a specific expense by its number
* Calculate total spending across all entries
* View spending totals grouped by category
* Instantly find your single highest expense
* Auto-save to a JSON file so nothing is lost between sessions
* Friendly error handling — invalid input, missing files, or interruptions (Ctrl+C) never crash the program

## 🧱 Core Components

Penniflect is a single-file script (`Penniflect.py`) organized into small, focused functions.

**Data Handling**
* `load_data()` — Loads saved expenses from `expenses.json` on startup, or starts fresh if none exist
* `save_data(expenses)` — Writes the current expense list back to `expenses.json`

**Menu & Flow**
* `display_menu()` — Prints the main menu of nine options
* `main()` — Runs the program loop, maps user choices to the right function, and handles saving on exit

**Expense Actions**
* `add_expense(expenses)` — Collects details for a new expense and appends it to the list
* `view_expenses(expenses)` — Displays every stored expense with a serial number
* `search_expense(expenses)` — Filters expenses by a category or description keyword
* `delete_expense(expenses)` — Removes a chosen expense from the list
* `calculate_total(expenses)` — Sums the amount of every expense
* `category_summary(expenses)` — Groups and totals spending by category
* `highest_expense(expenses)` — Finds the single largest expense

**Shared Helper**
* `print_expense(expense, index=None)` — Formats and prints a single expense consistently, reused across viewing, searching, and highest-expense display

## 📦 Data Model

Every expense is stored as a dictionary inside a single list:

```json
{
    "date": "2026-07-27",
    "category": "Food",
    "description": "Lunch",
    "amount": 12.5
}
```

All expenses persist in `expenses.json`, saved automatically whenever you choose *Save Data* or exit the program.

## 📁 Folder Structure

* `Penniflect.py` — The entire application: menu, data handling, and all expense operations
* `expenses.json` — Auto-generated data file where your expenses are stored (created on first save)

## 🚀 Getting Started

1. Clone this repository
2. Make sure you have **Python 3** installed
3. Run the program:
   ```bash
   python Penniflect.py
   ```
4. Follow the on-screen menu to add and manage your expenses

## 🛠 Dependencies

* Python 3
* Standard library only — `json` and `os` (no third-party packages required)

## 🔮 Future Enhancements

* Edit existing expenses instead of only deleting them
* Graphs and charts to visualize spending habits
* Better input validation on the menu
* A login system to support multiple users
* Export/import expenses as CSV or Excel
* A web-based version with forms and interactive charts

## 📜 License

MIT License

## 👤 Author

Hussain Kazmi
Computer Science student at Cedar College.

Built to make tracking everyday expenses simple — because knowing where your money goes is the first step to managing it.

