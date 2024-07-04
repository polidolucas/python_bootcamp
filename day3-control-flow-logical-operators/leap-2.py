year = int(input("Digite o ano: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Ano bissexto")
        else:
            print("Não é um ano bissexto")
    else:
        print("Ano bissexto")
else:
    print("Não é um ano bissexto")