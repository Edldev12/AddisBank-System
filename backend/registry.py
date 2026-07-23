def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class AccountRegistry:
    def __init__(self):
        self.by_number = {}
        self.order = []

    def add(self, account):
        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    # O(log n) search using Binary Search
    def find_by_number(self, number):
        numbers = sorted(self.by_number.keys())

        index = binary_search(numbers, number)

        if index == -1:
            return None

        return self.by_number[numbers[index]]

    # Leaderboard
    def top_by_balance(self, n=5):
        accounts = sorted(
            self.by_number.values(),
            key=lambda account: account.balance,
            reverse=True
        )

        return accounts[:n]
    
    def recursive_total(self, history, index=0):
        if index == len(history):
            return 0

        return history[index][1] + self.recursive_total(history, index + 1)
    # Recursive transaction total
    def total_transactions(self, number):
        account = self.find_by_number(number)

        if account is None:
            return 0

        return self.recursive_total(account.history)

    def list_all(self):
        return [self.by_number[number] for number in self.order]