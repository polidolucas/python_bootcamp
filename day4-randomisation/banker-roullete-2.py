import random

nomes = input("Digite o nome das pessoas que vão pagar a conta separados por vírgula: ")
nomes_lista = nomes.split(",")
a = len(nomes_lista) - 1
conta = random.randint(0,a)
print(f"Quem vai pagar a conta é {nomes_lista[conta]}.")