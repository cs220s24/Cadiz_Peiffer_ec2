import unittest
from unittest.mock import patch, Mock
import requests

# Define the base URL of your Flask server
BASE_URL = 'http://localhost:8000'

class TestFlaskApp(unittest.TestCase):
    # Test for the '/' endpoint
    @patch('requests.get')
    def test_hello_endpoint(self, mock_get):
        # Mock the response from the server
        mock_response = Mock(status_code=200)
        mock_response.text = '<h1 style="color:red">Hello World! 1</h1>'
        mock_get.return_value = mock_response

        # Send a GET request to the mock server
        response = requests.get(BASE_URL)

        # Assertions
        self.assertEqual(response.status_code, 200)  # Check if the status code is 200 (OK)
        self.assertIn('Hello World!', response.text)  # Check if the response contains 'Hello World!'
        self.assertIn('color:red', response.text)  # Check if the response contains 'color:red'

# This is required for running the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
