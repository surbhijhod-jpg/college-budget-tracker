class BudgetTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self, name, category, amount):
        new_expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        self.expenses.append(new_expense)

    def delete_expense(self, number):
        if number >= 1 and number <= len(self.expenses):
            self.expenses.pop(number - 1)
            return True

        return False

    def get_total(self):
        total_amount = 0

        for expense in self.expenses:
            total_amount += expense["amount"]

        return total_amount

    def get_category_total(self, category):
        total_amount = 0

        for expense in self.expenses:
            if expense["category"].lower() == category.lower():
                total_amount += expense["amount"]

        return total_amount