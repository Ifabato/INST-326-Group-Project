import csv
import os

FILE_NAME = "expenses.csv"

def initialize_file():
    """Ensure the CSV file exists and has the right header."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    """Add a new expense to the CSV file."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Utilities): ")
    description = input("Enter a description: ")
    amount = input("Enter the amount: ")
    
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")
