print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

countT = name1.count("t") + name2.count("t")
countR = name1.count("r") + name2.count("r")
countU = name1.count("u") + name2.count("u")
countE = name1.count("e") + name2.count("e")
countL = name1.count("l") + name2.count("l")
countO = name1.count("o") + name2.count("o")
countV = name1.count("v") + name2.count("v")

true = countT + countR + countU + countE
love = countL + countO + countV + countE
total = int(str(true) + str(love))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")