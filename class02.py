class Item():
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    def buy(self, count, price):
        self.count = count
        self.price = price
        if (self.count > 3):
            self.price = self.price//2
            return self.price
        else:
            return self.price
    
peach = Item("もも",5)
print(peach.name)
print(peach.stock)
peach.buy(20,500)
print(peach.price)