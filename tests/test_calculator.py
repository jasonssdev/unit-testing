import unittest
from src.calculator import addition, subtraction, multiplication, division

# To test run bellow command in terminal
# python3 -m unittest tests/test_calculator.py
# To run all tests in the tests directory, you can use the discover command:
# python3 -m unittest discover -s tests

class CalculatorTests(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(1 - 1, 0)

    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)

    def test_division(self):
        self.assertEqual(4 / 2, 2)