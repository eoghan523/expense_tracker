import requests  #imports rquests module neeeded for handling http requests.

BASE_URL = "http://127.0.0.1:5000/expenses"



def view_expenses():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        expenses = response.json().get('expenses', [])
        for expense in expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Date: {expense['date']}")
    
    else:
        print("Error retrieving expenses: ", response.status_code)


def add_expense(description, amount, date):    #Add Expense function which defines the add expense dictionary key-pairs.
    new_expense = {
        "Description": description,
        "Amount":     amount,
        "Date":       date
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
        print("Expense udpdated:", response.status_code)


