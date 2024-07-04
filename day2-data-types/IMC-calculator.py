height = input("Qual a sua altura? ")
weight = input("Qual o seu peso? ")

height = float(height)
weight = int(weight)

imc = int(weight / (height ** 2))
print(imc)