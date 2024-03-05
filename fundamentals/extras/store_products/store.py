from product import Product
class Store: 
    def __init__(self, name0):
        self.name = name0
        self.product_list = []
    def add_product(self, new_product, name1, price, category):
        new_product = Product(name1, price, category)
        self.product_list.append(new_product)
        return self
    def sell_product(self, id):
        self.product_list.pop(id+1)
        print(f"The {self.product_list[id]} was removed")
        return self
    def __str__(self):
        return print(f"The {self.product_list[id]} was removed")
    def inflation(self,percent_increase):
        for i in range(0, len(self.product_list)):
            self.product_list[i].update_price(percent_increase, True)
        return self
    def set_clearence(self, category, percent_discount):
        for i in range(0, len(self.product_list)):
            if self.product_list[i].category == category : 
                self.product_list[i].update_price(percent_discount, False)
        return self 





