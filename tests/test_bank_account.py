import unittest, os
from src.bank_account import BankAccount

# To run the tests, execute the following command:
# python3 -m unittest discover -v -s tests 


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transactions_log.txt")

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_transactions(self, filename):
        with open(filename, 'r') as file:
            return len(file.readlines())

    def test_deposit(self):
        self.assertEqual(self.account.deposit(100), 1100)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(150), 850)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_log_transaction(self):
        self.account.deposit(70)
        # self.account.withdraw(55)
        # self.account.get_balance()
        self.assertTrue(os.path.exists(self.account.log_file))

    def test_count_transactions(self):
        self.account.deposit(70)
        self.account.withdraw(55)
        self.account.get_balance()
        self.assertEqual(self._count_transactions(self.account.log_file), 4)
