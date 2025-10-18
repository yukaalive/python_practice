from random import randint
for i in range(100):
    dice = randint(1, 6)
    if dice == 1:
        print(i,"回目にして1きました")
        # break
        continue
    print(dice)

