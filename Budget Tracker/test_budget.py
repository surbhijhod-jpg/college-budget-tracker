from budget import BudgetTracker

tracker = BudgetTracker()

tracker.add_expense("Lunch", "Food", 100)
tracker.add_expense("Book", "Books", 50)

total = tracker.get_total()

if total == 150:
    print("Total is correct")
else:
    print("Total is wrong")

food = tracker.get_category_total("Food")

if food == 100:
    print("Food is correct")
else:
    print("Food is wrong")

tracker.delete_expense(1)

total = tracker.get_total()

if total == 50:
    print("Delete is working")
else:
    print("Delete is not working")

print("Done")