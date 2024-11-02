import requests  #imports rquests module neeeded for handling http requests.

BASE_URL = "http://127.0.0.1:5000/expenses"





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


def view_expenses():
    response = requests.get(BASE_URL)
    if 




