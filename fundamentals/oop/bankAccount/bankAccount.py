class BankAccount:
    allaccounts = []
    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance = balance
        BankAccount.allaccounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount < self.balance :
            self.balance -= amount 
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
        return self
    
    def display_account_info(self):
        print(f"Balance = {self.balance}")
        return self
    
    def yield_interest(self):
        while self.balance > 0 :
            self.balance += (self.balance) * (self.int_rate)
            return self
    @classmethod
    def printinfo(cls):
        for account in cls.allacounts :
            print(account.display_account_info())

first_account = BankAccount(0.01, 0)
second_account= BankAccount(0.01, 20)
print(first_account.balance)

first_account.deposit(50).deposit(20).deposit(30).withdraw(20).yield_interest().display_account_info()

second_account.deposit(100).deposit(200).withdraw(20).withdraw(50).withdraw(40).withdraw(50).yield_interest().display_account_info()

BankAccount.printinfo()