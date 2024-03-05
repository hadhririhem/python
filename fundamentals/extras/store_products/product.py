class Product : 
    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category 
    def update_price(self,percent_change,is_increased):
        if is_increased == True :
            self.price += percent_change
            print(f"{self.name}'s new price is {self.price}")
        else :
            self.price -= percent_change
            print(f"{self.name}'s new price is {self.price}")
        return self
    def print_info(self):
        print(f"The product's name is {self.name} from {self.category} and it's {self.price}$")
        return self

