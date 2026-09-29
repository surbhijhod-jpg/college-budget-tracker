# College Budget Tracker

## 1. Project Title

**College Budget Tracker**

## 2. Project Overview

College students have to manage their daily expenses such as food, travel, books, and other needs. It can be difficult to keep track of how much money is being spent.

The **College Budget Tracker** is a simple Python-based project that helps students record and manage their expenses. The user can add expenses, view all expenses, delete an expense, and see a simple spending report.

The project is designed using basic Python concepts and is easy to understand and use.

## 3. Features

The project provides the following features:

* Add a new expense
* View all recorded expenses
* Delete an expense
* Calculate total spending
* View category-wise spending
* Validate user input
* Display clear error messages for invalid input

## 4. Technologies Used

* Python
* Python functions
* Python classes
* Lists
* Dictionaries
* Conditional statements
* Loops
* Exception handling

No external Python libraries are required.

## 5. Project Files

### `main.py`

Contains the main menu and controls the overall program flow.

### `budget.py`

Contains the `BudgetTracker` class and functions for:

* Adding expenses
* Deleting expenses
* Calculating total spending
* Calculating category-wise spending

### `expenses.py`

Contains functions for:

* Adding expenses
* Viewing expenses
* Deleting expenses

### `reports.py`

Generates the budget report and displays category-wise spending.

### `validation.py`

Contains basic functions for checking user input.

### `test_budget.py`

Contains simple tests to check whether the main budget functions are working correctly.

## 6. How to Run the Project

### Step 1

Make sure Python is installed on your computer.

### Step 2

Open the project folder.

### Step 3

Open the terminal or command prompt in the project folder.

### Step 4

Run:

```bash
python main.py
```

The College Budget Tracker menu will appear.

## 7. How to Use

After starting the program, the following menu is displayed:

```text
===== COLLEGE BUDGET TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. View Budget Report
5. Exit
```

### Add Expense

Select option `1` and enter:

* Expense name
* Category
* Amount

### View Expenses

Select option `2` to see all recorded expenses.

### Delete Expense

Select option `3` and enter the number of the expense you want to delete.

### View Budget Report

Select option `4` to see:

* Total spending
* Food spending
* Travel spending
* Books spending
* Other spending

### Exit

Select option `5` to close the program.

## 8. Testing

The file `test_budget.py` contains basic tests for the budget calculations and delete operation.

Run it using:

```bash
python test_budget.py
```

If everything is working correctly, the following message will be displayed:

```text
All basic tests passed successfully.
```

## 9. Input Validation

The project handles common invalid inputs.

For example:

* Empty expense names are rejected.
* Empty categories are rejected.
* Negative amounts are rejected.
* Zero amounts are rejected.
* Invalid numbers are handled without crashing the program.
* Invalid expense numbers are rejected.

## 10. Project Objective

The main objective of this project is to provide a simple way for college students to manage their daily expenses while demonstrating basic Python programming concepts.

## 11. Future Improvements

The project can be improved in the future by adding:

* Monthly budgets
* Saving expenses between program sessions
* Graphs and charts
* Search and filter options
* More detailed reports
* A graphical user interface
