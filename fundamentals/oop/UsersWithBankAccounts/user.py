class User :
    def __init__(self, name ,account_balance):
        self.name = name
        self.account_balance= account_balance

    def make_deposit(self,amount):
        self.account_balance += amount

    
    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount
    
    def display_user_balance(self) :
        print(f" User: {self.name}, Balance: {self.account_balance}")
    