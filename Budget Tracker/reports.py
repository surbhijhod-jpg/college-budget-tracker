def show_report(tracker):

    print()
    print("My Budget Report")
    print()

    food = tracker.get_category_total("Food")
    travel = tracker.get_category_total("Travel")
    books = tracker.get_category_total("Books")
    other = tracker.get_category_total("Other")

    print("Food =", food)
    print("Travel =", travel)
    print("Books =", books)
    print("Other =", other)

    total = tracker.get_total()

    print()
    print("Total =", total)