class BankAccount:
    balance = 0
    int_rate = 0.01
    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance = balance

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
        