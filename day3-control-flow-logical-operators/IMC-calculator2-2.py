peso = int(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))

imc = round(float((peso / (altura ** 2))), 2)
#print(f"O seu IMC é {imc}")

if imc < 18.5:
    print(f"O seu IMC é {imc}. Voce está abaixo do peso")
else:
    if imc >= 18.5 and imc < 25:
        print(f"O seu IMC é {imc}. Voce está no peso normal")
    else:
        if imc >= 25 and imc < 30:
            print(f"O seu IMC é {imc}. Voce está um pouco acima do peso")
        else:
            if imc >= 30 and imc < 35:
                print(f"O seu IMC é {imc}. Voce está obeso")
            else:
                print(f"O seu IMC é {imc}. Voce é clinicamente muito obeso")    