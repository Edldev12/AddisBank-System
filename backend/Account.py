from config import config

class Account:

    account_counter = 1000

    def __init__(self, owner, balance):

        Account.account_counter += 1

        self.account_number = str(Account.account_counter)
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            return True

        return False


    def statement(self):

        return f"""
--- Account Statement ---
Owner: {self.owner}
Account Number: {self.account_number}
Balance: {self.balance} ETB
"""


class SavingsAccount(Account):

    def __init__(self, owner, balance):
        super().__init__(owner, balance)


    def add_interest(self):
        self.balance += self.balance * 0.07



class CurrentAccount(Account):

    def __init__(self, owner, balance):
        super().__init__(owner, balance)


    def withdraw(self, amount):

        if amount <= self.balance + 1000:
            self.balance -= amount
            return True

        return False