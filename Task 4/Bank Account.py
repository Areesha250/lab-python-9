class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account1 = BankAccount("Areesha", 5000)

account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()