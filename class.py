# クラス → オブジェクト → インスタンス
class Item:
    # コンストラクタ：初期化
    # selfは必ずself
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

peach = Item("もも", 3)
print(peach.name)
print(peach.stock)

pen = Item("ペン", 2)
print(pen.name)