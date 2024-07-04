target = int(input("Inisira o número limite: "))

total = 0
for i in range(2, (target + 1), 2):
    total += i
print(total)