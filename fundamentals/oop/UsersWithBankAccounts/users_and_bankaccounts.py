'''
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

'''
'''
class User :
    def __init__(self, name, int_rate, amount):
        self.name = name
        self.account = BankAccount(int_rate,amount)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self) :
        self.account.display_account_info()
        return self

    
#Sensei Bonus

class User :
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    def create_account(self, id, int_rate,amount):
        self.accounts[id]= BankAccount(int_rate, amount)

    def make_deposit(self, amount):
        if self.accounts[id] != None :
            self.accounts[id].deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        if self.accounts[id] != None :
            self.accounts[id].withdraw(amount)
        return self
    
    def display_user_balance(self) :
        if self.accounts[id] != None :
            self.accounts[id].display_account_info()
        return self

'''

import bank_account
class User(BankAccount):
    pass

USER1 = User(0.01,80)
USER1.display_account_info()


