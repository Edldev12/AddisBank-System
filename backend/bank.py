from abc import ABC,abstractmethod
from Account import SavingsAccount, CurrentAccount, Account

class observer(ABC):
    @abstractmethod
    def update(self, accunt, message):
        pass

class SMS(observer):
    def update(self, account, message):
         print(f"SMS -> {account.owner}: {message}")

class AuditLog(observer):

    def update(self, account, message):
        print(f"AUDIT -> Account {account.account_number}: {message}")



class AlertService:
    @staticmethod
    def send_alert(message):
        print(f"ALERT: {message}")

class AccountFactory:
    @staticmethod
    def create(account_type, owner, account_number, balance,  **kwarges):  #**kwarge pass multipla value
        if account_type == "savings":
            return SavingsAccount(owner, account_number, balance)

        elif account_type == "current":
            return CurrentAccount(owner, account_number, balance)

        else:
            return Account(owner, account_number, balance)