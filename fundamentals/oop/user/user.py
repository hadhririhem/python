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
    
    

user1 = User("Jihen", 0)
user2 = User("Rihem", 0)
user3 = User("Rami", 0)

user1.make_deposit(30)
user1.make_deposit(90)
user1.make_deposit(30)
user1.make_withdrawal(20)
user1.display_user_balance()

user2.make_deposit(50)
user2.make_deposit(150)
user2.make_withdrawal(50)
user2.make_withdrawal(50)
user2.display_user_balance()

user3.make_deposit(50)
user3.make_withdrawal(20)
user3.make_withdrawal(20)
user3.make_withdrawal(20)
user3.display_user_balance()

user1.transfer_money(user3,50)
user1.display_user_balance()
user3.display_user_balance()


