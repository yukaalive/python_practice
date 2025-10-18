class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getTaxPrice(self):
        return int(self.price * 1.1)
    
class Food(Item):
    def __init__(self, name, price, limit_date):
        super().__init__(name, price)
        self.limit_date = limit_date

    def getTaxPrice(self):
        return int(self.price * 1.08)
    
class Goods(Item):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
    def present(self):
        if self.color == "ブラック":
            return("男向けだよ")

peach = Food("桃", 600, 4)
print(peach.getTaxPrice())

pen = Goods("ペン", 200 , "ブラック")
print(pen.getTaxPrice())
print(pen.color)
print(pen.present())
