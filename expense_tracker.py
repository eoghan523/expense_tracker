import requests  #imports rquests module neeeded for handling http requests.


response = requests.get('https://github.com/eoghan523/expense_tracker')
print(response.status_code)  # Status code of the response
print(response.json())  # JSON response if available
