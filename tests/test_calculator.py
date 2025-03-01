import unittest
from src.calculator import sum, subtract, multiply, divide
# To test run bellow command in terminal
# python3 -m unittest tests/test_calculator.py
# To run all tests in the tests directory, you can use the discover command:
# python3 -m unittest discover -s tests
class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_multiply(self):
        assert multiply(3, 2) == 6

    def test_divide(self):
        result = divide(10, 2)
        expected = 5
        assert result == expected

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)