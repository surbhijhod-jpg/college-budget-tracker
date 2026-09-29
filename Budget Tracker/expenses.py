def add_expense(tracker):

    print("\n--- Add Expense ---")

    name = input("What did you buy? ")

    if name == "":
        print("Name cannot be empty.")
        return

    category = input("Which category? ")

    if category == "":
        print("Category cannot be empty.")
        return

    amount = input("How much did it cost? ")

    try:
        amount = float(amount)
    except:
        print("Enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    tracker.add_expense(name, category, amount)

    print("Expense added.")


def view_expenses(tracker):

    print("\n--- My Expenses ---")

    if len(tracker.expenses) == 0:
        print("No expenses yet.")
        return

    i = 1

    for expense in tracker.expenses:

        print(
            i,
            ".",
            expense["name"],
            "|",
            expense["category"],
            "| Rs.",
            expense["amount"]
        )

        i = i + 1


def delete_expense(tracker):

    print("\n--- Delete Expense ---")

    if len(tracker.expenses) == 0:
        print("Nothing to delete.")
        return

    view_expenses(tracker)

    number = input("Which expense do you want to delete? ")

    try:
        number = int(number)
    except:
        print("Please enter a number.")
        return

    result = tracker.delete_expense(number)

    if result == True:
        print("Expense deleted.")
    else:
        print("Wrong expense number.")