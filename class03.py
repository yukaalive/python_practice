class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Food(Item):
    def __init__(self, name, price, limit_date):
        super().__init__(name, price)
        self.limit_date = limit_date

class Goods(Item):
    pass

peach = Food("桃", 600, 4)
print(peach.limit_date)

pen = Goods("ペン", 200)