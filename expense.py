expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense Added Successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n----- Expense List -----")

    total = 0

    for expense in expenses:
        print(f"{expense['name']} : ₹{expense['amount']}")
        total += expense['amount']

    print("------------------------")
    print("Total Expense: ₹", total)
    print()


while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.\n")