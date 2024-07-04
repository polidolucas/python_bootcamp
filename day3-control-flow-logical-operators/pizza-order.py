print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N? ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N? ") # Do you want extra cheese? Y or N

small = 15
medium = 20
large = 25

if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            small += 3
            print(f'Your final bill is: ${small}.')
        else:
            small += 2
            print(f'Your final bill is: ${small}.')
    else:
        if extra_cheese == 'Y':
            small += 1
            print(f'Your final bill is: ${small}.')
        else:
            print(f'Your final bill is: ${small}.')

if size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            medium += 4
            print(f'Your final bill is: ${medium}.')
        else:
            medium += 3
            print(f'Your final bill is: ${medium}.')
    else:
        if extra_cheese == 'Y':
            medium += 1
            print(f'Your final bill is: ${medium}.')
        else:
            print(f'Your final bill is: ${medium}.')

if size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            large += 4
            print(f'Your final bill is: ${large}.')
        else:
            large += 3
            print(f'Your final bill is: ${large}.')
    else:
        if extra_cheese == 'Y':
            large += 1
            print(f'Your final bill is: ${large}.')
        else:
            print(f'Your final bill is: ${large}.')