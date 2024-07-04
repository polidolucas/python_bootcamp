import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
computer = random.randint(0,2)

if choice == 0:
    if computer == 0:
        print(f"{rock}\nComputer choose{rock}\nIt's a draw")
    else:
        if computer == 1:
            print(f"{rock}\nComputer choose{paper}\nYou lose")
        else:
            print(f"{rock}\nComputer choose{scissors}\nYou win")
else:
    if choice == 1:
        if computer == 0:
            print(f"{paper}\nComputer choose{rock}\nYou win")
        else:
            if computer == 1:
                print(f"{paper}\nComputer choose{paper}\nIt's a draw")
            else:
                print(f"{paper}\nComputer choose{scissors}\nYou lose")
    else:
        if choice == 2:
            if computer == 0:
                print(f"{scissors}\nComputer choose{rock}\nYou lose")
            else:
                if computer == 1:
                    print(f"{scissors}\nComputer choose{paper}\nYou win")
                else:
                    print(f"{scissors}\nComputer choose{scissors}\nIt's a draw")
        else:
            print("Wrong choice!")