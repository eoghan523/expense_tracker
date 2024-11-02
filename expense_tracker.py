import requests  #imports rquests module neeeded for handling http requests.

BASE_URL = "http://127.0.0.1:5000/expenses"           #This is the API/ URL pointed towards the flask server running in app.py and listening on port 5000. 



def view_expenses():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        expenses = response.json().get('expenses', [])
        for expense in expenses:
            print(f"ID: {expense['id']}, description: {expense['description']}, amount: {expense['amount']}, date: {expense['date']}")
    
    else:
        print("Error retrieving expenses: ", response.status_code)


def add_expense(description, amount, date):    #Add Expense function which defines the add expense dictionary key-pairs.
    new_expense = {
        "description": description,
        "amount":     amount,
        "date":       date
    }
    response = requests.post(BASE_URL, json=new_expense)
    if response.status_code == 201:
        print("Expense added successfully:", response.json())

    else:
        print("Error adding your response.", response.status_code)

def update_expense(expense_id, description, amount, date):
    """Update to an existing expense."""
    updated_expense = {
        "description": description,
        "amount": amount,
        "date": date
    }
    response = requests.put(f"{BASE_URL}/{expense_id}", json=updated_expense)
    if response.status_code == 200:
        print("Expense udpdated:", response.json())
    
    else:
        print("Error in updating expense:", response.status_code)

def delete_expense(expense_id):
    """"Delete an expense function."""
    response =  requests.delete(f"{BASE_URL}/{expense_id}")
    if response.status_code == 204:
        print("Expense deleted successfully.")
    
    else: 
        print("Error in deleting expense: ", response.status_code)


def main():
    """Main expense tracker function."""
    while True:

        print("============================")
        print("|    Expense Tracker app    |")
        print("============================")
        print("1. View Expenses")
        print("2. Add an Expense")
        print("3. Update an Expense")
        print("4. Delete an Expense")
        print("5. Exit")

        user_choice = input("Please select an option (1-5): ")

        if user_choice == '1':
            view_expenses()
        
        elif user_choice == '2':
            description = input("Enter your expense description: ")
            while True:
                try: 
                    amount = float(input("Enter an amount: £"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric amount.")
           
            date  = input("Enter expense date (DD-MM-YYYY): ")
            add_expense(description, amount, date)

        elif user_choice == '3':
            while True:
                try:
                    expense_id = int(input("Enter expense ID to update: "))
                    break  # Valid input, exit the loop
                except ValueError:
                    print("Invalid input. Please enter a numeric expense ID.")

            description = input("Enter new expense description: ")
            amount = float(input("Enter new expense amount: "))
            date = input("Enter new expense date (YYYY-MM-DD): ")
            update_expense(expense_id, description, amount, date)

        elif user_choice == '4':
            while True:
                try:
                    expense_id = int(input("Enter expense ID to delete: "))
                    break  # Valid input, exit the loop
                except ValueError:
                    print("Invalid input. Please enter a numeric expense ID.")
            delete_expense(expense_id)


        elif user_choice == '5':
            break
        else:
            return ValueError("Invalid option. Please enter a valid response...")

if __name__ == '__main__':
    main()


     




