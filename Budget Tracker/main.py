from budget import BudgetTracker
from expenses import add_expense, view_expenses, delete_expense
from reports import show_report


tracker = BudgetTracker()


def menu():

    print("\n--- College Budget Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. View Report")
    print("5. Exit")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(tracker)

    elif choice == "2":
        view_expenses(tracker)

    elif choice == "3":
        delete_expense(tracker)

    elif choice == "4":
        show_report(tracker)

    elif choice == "5":
        print("Thank you!")
        print("Have a nice day.")
        break

    else:
        print("Please choose a number from 1 to 5.")