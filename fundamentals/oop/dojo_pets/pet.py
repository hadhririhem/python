class Pet :
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping and her energy level is {self.energy}")
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating, her energy and health level are {self.energy} and {self.health}")
        return self
    def play(self):
        self.health += 5
        print(f"{self.name} is playing and her health rate is {self.health}")
        return self
    def noise(self):
        print(f"I'm hearing a {self.type}'s sound")

class Cat(Pet): 
    def __init__(self, name, type , tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
    def sleep(self):
        super().sleep()
        if self.type.lower()== "cat":
            print(f"{self.name} is sleeping and we can hear grrrrr")
        return self
'''
katous = Cat("katous","CaT","None", 50, 50)
katous.sleep()
katous.play()
'''