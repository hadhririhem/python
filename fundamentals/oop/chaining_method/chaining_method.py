class User :
    def __init__(self, name ,account_balance):
        self.name = name
        self.account_balance= account_balance

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount
        return self
    
    def display_user_balance(self) :
        print(f" User: {self.name}, Balance: {self.account_balance}")
        return self
    

user1 = User("Jihen", 0)
user2 = User("Rihem", 0)
user3 = User("Rami", 0)

user1.make_deposit(30).make_deposit(90).make_deposit(30).make_withdrawal(20).display_user_balance()

user2.make_deposit(50).make_deposit(150).make_withdrawal(50).make_withdrawal(50).display_user_balance()

user3.make_deposit(50).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).display_user_balance()

user1.transfer_money(user3,50).display_user_balance()
user3.display_user_balance()