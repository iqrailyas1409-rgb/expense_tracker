import csv
import os

FILE_NAME = "expenses.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount"])


def add_expense():
    category = input("Enter Expense Category: ")
    amount = input("Enter Amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

    print("Expense added successfully!")


def view_expenses():
    print("\n----- Expense List -----")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        found = False
        for row in reader:
            found = True
            print(f"Category: {row[0]} | Amount: ₹{row[1]}")

        if not found:
            print("No expenses found.")


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expenses: ₹{total}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
        print("Expense Tracker")