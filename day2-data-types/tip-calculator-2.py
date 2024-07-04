conta = float(input("Digite o valor total da conta. $"))
gorjeta = int(input("Qual o valor da gorjeta que gostaria de dar? 10%, 12% ou 15%? "))
pessoas = int(input("Quantas pessoas irão dividir a conta? "))

divisao = round(((conta * ((gorjeta / 100) + 1 )) / pessoas), 2)
print(f"A conta ficou ${divisao} para cada")