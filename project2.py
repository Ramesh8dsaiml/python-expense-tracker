import csv

expensesList = []
print("Welcome to Expense Tracker (CSV Version)")

file_name = "expenses.csv"  # save data in csv file 

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter expense date: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = [date, category, description, amount]

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expense)

        print("Expense saved to file successfully.")

    elif choice == 2:
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                print("\nDate | Category | Description | Amount")
                print("--------------------------------------")
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("No expense file found.")

    elif choice == 3:
        total = 0
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    total += float(row[3])
            print(f"\nTotal Spending: {total}")
        except FileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == 4:
        print("Exiting system. Have a nice day!")
        break

    else:
        print("Invalid choice.")
