import unittest  # Import the unittest module to create and run tests
from unittest.mock import patch  # Import patch to mock external dependencies
import requests  # Import the requests library to make HTTP requests
import sys  # Import sys to manipulate the Python runtime environment
import os  # Import os for file path manipulations

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Absolute import from the parent directory

class TestExpenseTracker(unittest.TestCase):

    @patch('requests.get')  # Mock the requests.get method to simulate API calls
    def test_get_expense_not_found(self, mock_get): # Define a test method for simulating a 404 error
        # Mock the response to simulate a 404 error
        mock_get.return_value.status_code = 404  
        mock_get.return_value.json.return_value = {"error": "Not found"}   # Sets the mocked JSON response
        #GET request to a URL that simulates an expense not found
        response = requests.get('http://127.0.0.1:5000/expenses/999')

        self.assertEqual(response.status_code, 404)
         # Assert that the JSON response matches the expected error message
        self.assertEqual(response.json(), {"error": "Not found"})

    @patch('requests.post')   # Mock the requests.post method to simulate API calls
    def test_add_expense(self, mock_post):
        # Mock the response for adding an expense
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {         # Set the mocked JSON response to as follows below
            "id": 1,
            "description": "Lunch",
            "amount": 10.5,
            "date": "2023-11-01"
        }

         # Make a POST request to add a new expense
        response = requests.post('http://127.0.0.1:5000/expenses', json={
            "description": "Lunch",
            "amount": 10.5,
            "date": "2023-11-01"
        })

        self.assertEqual(response.status_code, 201)              
        self.assertEqual(response.json(), {                      # Assert that the JSON response matches the expected expense data
            "id": 1,
            "description": "Lunch",
            "amount": 10.5,
            "date": "2023-11-01"
        })

if __name__ == '__main__':
    unittest.main()
