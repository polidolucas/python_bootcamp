line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Ex: A1.: ") # Where do you want to put the treasure?

position_split = list(position) #criar uma lista a partir do input
x = position_split[0] #pegar o primero item da lista e colocar em uma variável
y = int(position_split[1]) #pegar o segundo item da lista e colocar em uma variável

if x == "A":
    if y == 1:
        line1[0] = " X"
    else:
        if y == 2:
           line2[0] = " X" 
        else:
            if y == 3:
                line3[0] = " X"
            else:
                print("Wrong number!")

else:
    if x == "B":
        if y == 1:
            line1[1] = " X"
        else:
            if y == 2:
                line2[1] = " X"
            else:
                if y == 3:
                    line3[1] = " X"
                else:
                    print("Wrong number!")
    else:
        if x == "C":
            if y == 1:
                line1[2] = " X"
            else:
                if y == 2:
                    line2[2] = " X"
                else:
                    if y == 3:
                        line3[2] = " X"
                    else:
                        print("Wrong number!")
        else:
            print("Wrong input!")

# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")