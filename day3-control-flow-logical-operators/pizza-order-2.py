print("Bem vindo a pizzaria do Skywalker")
print("Tamanhos: Pequena (P): $15 | Media (M): $20 | Grande (G): $25")
tamanho = input("Qual o tamanho da pizza que voce gostaria? ")
print("Pepperoni pizza Pequena +$2 | Media/Grande +$3")
pepperoni = input("Gostaria de adicionar pepperoni? ")
queijo = input("Gostaria de adicionar queijo? +$1 para qualquer tamanho: ")

p = 15
m = 20
g = 25

if tamanho == "P":
    if pepperoni == "Sim":
        if queijo == "Sim":
            p += 3
            print(f"O total da pizza é ${p}")
        else:
            p += 2
            print(f"O total da pizza é ${p}")
    else:
        if queijo == "Sim":
            p += 1
            print(f"O total da pizza é ${p}")
        else:
            print(f"O total da pizza é ${p}")
else:
    if tamanho == "M":
        if pepperoni == "Sim":
            if queijo == "Sim":
                m += 4
                print(f"O total da pizza é ${m}")
            else:
                m += 3
                print(f"O total da pizza é ${m}")
        else:
            if queijo == "Sim":
                m += 1
                print(f"O total da pizza é ${m}")
            else:
                print(f"O total da pizza é ${m}")
    else:
        if tamanho == "G":
            if pepperoni == "Sim":
                if queijo == "Sim":
                    g += 4
                    print(f"O total da pizza é ${g}")
                else:
                    g += 3
                    print(f"O total da pizza é ${g}")
            else:
                if queijo == "Sim":
                    g += 1
                    print(f"O total da pizza é ${g}")
                else:
                    print(f"O total da pizza é ${g}")

