import unittest               #Imports the unittest module for testing python code
from unittest.mock import patch #Imports the patch feature in unittest that can mock API resposes to simulate http requests.
import requests

#patch allows for the mocking of: requests.get, requests.post, requests.put, and requests.delete

class testFunction(unittest.TestCase):

    @patch('requests.get')                #Mocking a request.get
    def test_fuction(self, mock_get):
        mock_get.return_value.json.return_value = {"key": "value"}


if __name__ == '__main__':
    unittest.main()