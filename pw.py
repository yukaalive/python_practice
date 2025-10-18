from random import randint
seeds = [
    "A","B","C",
    "a","b","c",
    "1","2","3",
    "!","@","#"
]

length = int(input("何文字がいいですか"))
password = ""
for i in range(length):
    index = randint(0,len(seeds)-1)
    password += seeds[index]


print(password)