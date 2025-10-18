from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @abstractmethod
    def getTaxPrice(self):
        pass

class Food(Item):
    def getTaxPrice(self):
        return int(self.price * 1.08)

class Goods(Item):
    def getTaxPrice(self):
        return int(self.price * 1.08)

peach = Food("もも", 300)
print(peach.getTaxPrice())

pen = Goods("ペン",200)
print(pen.getTaxPrice())