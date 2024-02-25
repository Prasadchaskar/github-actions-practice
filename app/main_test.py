from main import return_reverse_str
import unittest
from fastapi.testclient import TestClient
import os
from main import app
import json

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    # This is updated test case
    def test_return_reverse_str(self):
        random_str = "prasad"
        expected_result = '"dasarp"'
        response = self.client.get(f"/{random_str}")
        print(response.text)  # Print response text to see its format
        self.assertEqual(response.text, expected_result)

if __name__ == "__main__":
    unittest.main()
