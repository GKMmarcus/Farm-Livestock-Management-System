class livestock:
    def __init__(self,age):
        self.age = age
    def get_age(self):
        return self.age
    def get_animal_type(self):
        return self.type
    def price(self):
        return 0
        
class Alpaca(livestock):
    def __init__(self,age=0,weigh=0):
        livestock.__init__(self,age)
        if weigh < 0:
            self.weigh = 0
        else:
            self.weigh = weigh
    def get_weigh(self):
        return self.weigh
    def get_price(self):
        if self.age <= 3:
            return 10000
        elif self.weigh < 300:
            return 80000
        else:
            return 100000
    def get_animal_type(self):
        return 'Alpca'

class Camel(livestock):
    def __init__(self,age=0,humps=0):
        livestock.__init__(self,age)
        if humps < 0:
            self.humps = 0
        else:
            self.humps = humps
    def get_humps(self):
        return self.humps
    def get_price(self):
        if self.age <= 3:
            return 50000
        elif self.humps == 2:
            return 150000
        elif self.humps == 3:
            return 200000
    def get_animal_type(self):
        return 'Camel'
    
class Donkey(livestock):
    def __init__(self,age,breed):
        self.breed = breed
        livestock.__init__(self,age)
    def get_breed(self):
        return self.breed
    def get_price(self):
        if self.age <= 3:
            return 20000
        elif self.breed == 'Miniature':
            return 100000
        elif self.breed == 'Burro':
            return 120000
        elif self.breed == 'American Mammoth Jacks':
            return 180000
    def get_animal_type(self):
        return 'Donkey'

class FarmApp:
    def __init__(self):
        self.livestockList = []
    def get_livestock(self):
        return self.livestockList
    def add_livestock(self,animal):
        self.livestockList.append(animal)
    def get_total_price(self):
        total_sum = 0
        for livestock in self.livestockList:
            total_sum += livestock.get_price()
        return total_sum
        

def main():
    farm = FarmApp()
    animal1 = Alpaca(5,600)
    animal2 = Camel(5, 3)
    animal3 = Donkey(6, "Miniature")
    farm.add_livestock(animal1)
    farm.add_livestock(animal2)
    farm.add_livestock(animal3) 
    animals = farm.get_livestock()
    print("List of Animals Sold") 
    print("====================\n")
    for animal in animals:
        print(animal.get_animal_type(), '\t$', animal.get_price())
    print("\nTotal sales \t$", farm.get_total_price(), "\n") 
    animal4 = Donkey(2, "American Mammoth Jack") 
    animal5 = Donkey(7, "Burro") 
    animal6 = Alpaca(2, 250) 
    farm.add_livestock(animal4)
    farm.add_livestock(animal5)
    farm.add_livestock(animal6)
    for animal in animals:
        print(animal.get_animal_type(), '\t$', animal.get_price())
    print("\nTotal sales \t$", farm.get_total_price()) 
main()

    
    











