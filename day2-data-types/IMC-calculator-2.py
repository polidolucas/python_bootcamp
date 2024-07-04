peso = int(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))

imc = round(float((peso / (altura ** 2))), 2)
print(f"O seu IMC é {imc}")