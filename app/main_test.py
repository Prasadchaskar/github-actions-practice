from main import return_reverse_str
import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_reverse_str(self):
        random_str = "prasad"
        random_str_reversed = "dasarp"
        self.assertEqual(random_str_reversed, return_reverse_str(random_str))

if __name__ == "__main__":
    unittest.main()
