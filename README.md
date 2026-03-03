Simple Budget App


This is a Python-based budget tracking tool I built to practice Object-Oriented Programming (OOP) and string manipulation. It helps you manage different spending categories, track a ledger of transactions, and visualize your spending habits.

What it does
Create Categories: Set up budgets for Food, Clothing, Entertainment, etc.

Track Transactions: Deposit funds with descriptions or withdraw them (with automatic balance checks).

Transfer Funds: Easily move money between categories (e.g., from "Paycheck" to "Savings").

Visual Reports: Prints a clean, formatted receipt for each category and generates a bar chart showing the percentage spent across all categories.

How to use it
The app uses a Category class. Here’s a quick snippet of how it looks in action:

Python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
