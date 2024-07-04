line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Onde você deseja colocar o tesouro? Ex.: A1, B2, C3..: ")
position_list = list(position)
pos_a = position_list[0]
pos_b = int(position_list[1])

print(f"{line1}\n{line2}\n{line3}")