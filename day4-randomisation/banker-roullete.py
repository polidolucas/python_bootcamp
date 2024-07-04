import random

names = input("Nome das pessoas separadas por virgula: ")
names_list = names.split(",")
a = len(names_list) - 1
select = random.randint(0,a)
#banker = names_list[select]
print(f"{names_list[select]} is going to buy the meal today!")