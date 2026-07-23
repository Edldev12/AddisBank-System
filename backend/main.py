from Account import *
from bank import *
from registry import *
from bank_model import *
from config import BankConfig

class AddisBank:

    def __init__(self):
        self.registry = AccountRegistry()
        self.transactions = []
        self.config = BankConfig()
        self.branch = None
    def show_menu(self):
        print("\n====== ADDIS BANK ======")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Find Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Check Balance")
        print("8. Transaction History")
        print("9. Top Accounts")
        print("10. Add Interest")
        print("11. Statistics")
        print("12. Branch Overview")
        print("13. Undo Transaction")
        print("0. Exit")

    def run(self):

        while True:

            self.show_menu()

            choice = input("Choose option: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.view_all_accounts()

            elif choice == "3":
                self.find_account()

            elif choice == "4":
                self.deposit_money()

            elif choice == "5":
                self.withdraw_money()

            elif choice == "6":
                self.transfer_money()

            elif choice == "7":
                self.check_balance()

            elif choice == "8":
                self.view_transactions()

            elif choice == "9":
                self.top_accounts()

            elif choice == "10":
                self.add_interest()

            elif choice == "11":
                self.view_statistics()

            elif choice == "12":
                self.branch_tree_overview()

            elif choice == "13":
                self.undo_transaction()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

    def get_input(self, prompt, input_type=str):

        while True:

            value = input(prompt)

            if value.lower() == "cancel":
                return None

            try:
                return input_type(value)

            except ValueError:
                print("Invalid input.")
    def create_account(self):

        owner = self.get_input("Owner: ")

        if owner is None:
            return

        balance = self.get_input("Initial Balance: ", float)

        if balance is None:
            return

        print("1. Savings")
        print("2. Current")
        print("3. Basic")

        choice = input("Choose account type: ")

        if choice == "1":
            account = SavingsAccount(owner, balance)

        elif choice == "2":
            account = CurrentAccount(owner, balance)

        elif choice == "3":
            account = Account(owner, balance)
        else:
            print("Invalid choice")
            return

        self.registry.add(account)

        print("Account created successfully.")
        print("Account Number:", account.account_number)

    def view_all_accounts(self):
        if not self.registry.order:
            print("\nNo accounts available.")
            return

        total = 0

        for number in self.registry.order:

            account = self.registry.by_number[number]

            print(account.statement())

            total += account.balance

        print(f"\nTotal Bank Balance: {total}")

    def find_account(self):

        number = self.get_input("Account Number: ")

        account = self.registry.find_by_number(number)

        if account:
            print(account.statement())
        else:
            print("Account not found.")

    def deposit_money(self):

        number = self.get_input("Account Number: ")

        account = self.registry.find_by_number(number)

        if not account:
            print("Not Found")
            return

        amount = self.get_input("Amount: ", float)

        account.deposit(amount)

        self.transactions.append(
            ("Deposit", number, amount)
        )

        print("Deposit successful.")

    def withdraw_money(self):

        number = self.get_input("Account Number: ")

        account = self.registry.find_by_number(number)

        if not account:
            return

        amount = self.get_input("Amount: ", float)

        if account.withdraw(amount):

            self.transactions.append(
                ("Withdraw", number, amount)
            )

            print("Success")

        else:
            print("Insufficient balance.")

    def check_balance(self):

        number = self.get_input("Account Number: ")

        account = self.registry.find_by_number(number)

        if account:
            print(account.balance)

    def transfer_money(self):

        sender = self.get_input("From: ")

        receiver = self.get_input("To: ")

        amount = self.get_input("Amount: ", float)

        acc1 = self.registry.find_by_number(sender)
        acc2 = self.registry.find_by_number(receiver)

        if not acc1 or not acc2:
            print("Account not found.")
            return

        if acc1.withdraw(amount):

            acc2.deposit(amount)

            self.transactions.append(
                ("Transfer", sender, receiver, amount)
            )

            print("Transfer successful.")

        else:
            print("Transfer failed.")

    def view_transactions(self):

        number = self.get_input("Account Number: ")

        for t in self.transactions:

            if number in t:
                print(t)

    def top_accounts(self):

        n = self.get_input("Top how many? ", int)

        accounts = sorted(
            self.registry.by_number.values(),
            key=lambda x: x.balance,
            reverse=True
        )

        for account in accounts[:n]:
            print(account.statement())

    def add_interest(self):

        number = self.get_input("Account Number: ")

        account = self.registry.find_by_number(number)

        if isinstance(account, SavingsAccount):

            account.add_interest()

            print("Interest Added.")

        else:
            print("Not a savings account.")

    def view_statistics(self):

        accounts = list(self.registry.by_number.values())

        total = sum(a.balance for a in accounts)

        average = total / len(accounts) if accounts else 0

        print(f"Total Accounts: {len(accounts)}")
        print(f"Total Balance: {total}")
        print(f"Average Balance: {average}")

        print("Savings:",
        sum(isinstance(a, SavingsAccount) for a in accounts))

        print("Current:",
            sum(isinstance(a, CurrentAccount) for a in accounts))

        print("Basic:",
            sum(isinstance(a, Account) for a in accounts))


    def branch_tree_overview(self):
        self.branch.display()
        print("Total Balance:", self.branch.total_balance())

    def undo_transaction(self):

        if not self.transactions:
            print("No transaction to undo.")
            return

        last = self.transactions.pop()

        print("Undoing:", last)

if __name__ == "__main__":
    bank = AddisBank()
    bank.run()