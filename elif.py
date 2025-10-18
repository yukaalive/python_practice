age = int(input("年齢を教えてね=>"))

if age < 10:
    print("子供料金です")
elif age >= 65:
    print("シニア料金です")
else:
    print("大人料金です")
