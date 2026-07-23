from  bank import *

class Account:
    def __init__(self, owner, account_number, balance = 0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.observers = []
        self.history = []     #Day 7: Transaction history stack

    # Read-only balance
    @property
    def balance(self):
        return self.__balance
    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(self, message)

        
    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(("deposit", amount))
            print("Deposit successful.")
            self.notify(f"Deposited {amount} ETB")
        else:
            print("deposit only posetive number.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            self.history.append(("withdraw", amount))
            print("Withdrawal successful.")
            self.notify(f"Withdrew {amount} ETB")
        
    
      # Undo last transaction
    def undo_last(self):
        if not self.history:
            print("No transaction to undo.")
            return

        transaction, amount = self.history.pop()

        if transaction == "deposit":
            self.__balance -= amount
            print(f"Undo deposit of {amount} ETB")

        elif transaction == "withdraw":
            self.__balance += amount
            print(f"Undo withdrawal of {amount} ETB")


    # Print account details
    def statement(self):
        print("\n--- Account Statement ---")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance, "ETB")



# day 5 large project update
# THOSE Classes are inhareted from day 4 class(Account)
              # child 1
# calculate interest
class SavingsAccount(Account):
    def __init__(Self, owner, account_number, balance=0, rate=0.07):
        super().__init__(owner, account_number, balance)
        Self.rate = config.interest_rate
   
       
    def add_interest(Self):
        Self.deposit(Self.balance * Self.rate)
    def statement(Self):
        super().statement()
        print(f"iterest rate: {Self.rate * 100}%")

                 # child 2
        
# calculate overdraft tell what is the max creadt depeand on current balance
class CurrentAccount(Account):
    def __init__(Self, owner, account_number, balance=0, overdraft=1000):
        super().__init__(owner, account_number, balance)
        Self.overdraft = overdraft
    def withdraw(Self, amount):
        if amount<0:
            print("enter posetive number")
        else:
            if amount > Self.balance + Self.overdraft:
                print("Overdraft limit exceeded")
            else:
                Self._Account__balance -= amount
                Self.history.append(("withdraw", amount))
                Self.notify(f"Withdrew {amount} ETB")
        
    def statement(self):
        super().statement()
        print(self.overdraft,"ETB")

