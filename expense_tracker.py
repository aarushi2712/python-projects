import csv

FILE_NAME = "expenses.csv"

def add_expense(amount, category):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])
    print("Expense added successfully!")

def view_expenses():
    total = 0
    category_totals = {}

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[0])
                category = row[1]
                total += amount
                category_totals[category] = category_totals.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses found.")
        return

    print("\nExpense Summary:")
    print(f"Total Spent: ${total:.2f}")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(amount, category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

main()
