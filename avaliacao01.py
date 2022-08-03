# Gabriel Augusto Tomasoni Gaede
# Exercício 01 - Conjuntos



conjuntoA = ""
conjuntoB = ""


def operacao(x):
    for indice in range(1, len(x),3):
        if "U" in x[indice]:
            uniao = []
            conjuntoA = x[indice + 1].replace(",", " ").split()
            conjuntoB = x[indice + 2].replace(",", " ").split()
            for a in conjuntoA:
                uniao.append(a)
            for b in conjuntoB:
                if (b in conjuntoA) == False:
                    uniao.append(b)
            conjuntoB = x[indice + 2].replace(",", " ").split()

            print("União: conjunto 1 {", end="")
            for a in range(len(conjuntoA)):
                if a == len(conjuntoA) - 1:
                    print(conjuntoA[a], end="")
                else:
                    print(conjuntoA[a], end=",")
            print("}, conjunto 2 {", end="")
            for a in range(len(conjuntoB)):
                if a == len(conjuntoB) - 1:
                    print(conjuntoB[a], end="")
                else:
                    print(conjuntoB[a], end=",")
            print("}. Resultado:", end=" {")
            for a in range(len(uniao)):
                if a == len(uniao) - 1:
                    print(uniao[a], end="")
                else:
                    print(uniao[a], end=",")
            print("}")
        if "I" in x[indice]:
            inter = []
            conjuntoA = x[indice + 1].replace(",", " ").split()
            conjuntoB = x[indice + 2].replace(",", " ").split()
            for num in range(len(conjuntoB)):
                if conjuntoB[num] in conjuntoA:
                    inter.append(conjuntoB[num])
            print("Interseção: conjunto 1 {", end="")
            for a in range(len(conjuntoA)):
                if a == len(conjuntoA) - 1:
                    print(conjuntoA[a], end="")
                else:
                    print(conjuntoA[a], end=",")
            print("}, conjunto 2 {", end="")
            for a in range(len(conjuntoB)):
                if a == len(conjuntoB) - 1:
                    print(conjuntoB[a], end="")
                else:
                    print(conjuntoB[a], end=",")
            print("}. Resultado:", end=" {")
            for a in range(len(inter)):
                if a == len(inter) - 1:
                    print(inter[a], end="")
                else:
                    print(inter[a], end=",")
            print("}")
        if "D" in x[indice]:
            dif = []
            conjuntoA = x[indice + 1].replace(",", " ").split()
            conjuntoB = x[indice + 2].replace(",", " ").split()
            for a in conjuntoA:
                if (a in conjuntoB) == False:
                    dif.append(a)
            conjuntoA = x[indice + 1].replace(",", " ").split()

            print("Diferença: conjunto 1 {", end="")
            for a in range(len(conjuntoA)):
                if a == len(conjuntoA) - 1:
                    print(conjuntoA[a], end="")
                else:
                    print(conjuntoA[a], end=",")
            print("}, conjunto 2 {", end="")
            for a in range(len(conjuntoB)):
                if a == len(conjuntoB) - 1:
                    print(conjuntoB[a], end="")
                else:
                    print(conjuntoB[a], end=",")
            print("}. Resultado:", end=" {")
            for a in range(len(dif)):
                if a == len(dif) - 1:
                    print(dif[a], end="")
                else:
                    print(dif[a], end=",")
            print("}")
        if "C" in x[indice]:
            prod = ""
            A = x[indice + 1].replace(",", " ").split()
            B = x[indice + 2].replace(",", " ").split()
            for a in range(len(A)):
                for b in range(len(B)):
                    if a == (len(A) - 1) and b == (len(B) - 1):
                        p = f"({A[a]};{B[b]})"
                        prod = prod + p
                    else:
                        p = f"({A[a]};{B[b]});"
                        prod = prod + p

            print("Produto Cartesiano: conjunto 1 {", end="")
            for a in range(len(A)):
                if a == len(A) - 1:
                    print(A[a], end="")
                else:
                    print(A[a], end=",")
            print("}, conjunto 2 {", end="")
            for a in range(len(B)):
                if a == len(B) - 1:
                    print(B[a], end="")
                else:
                    print(B[a], end=",")
            print("}. Resultado: {", prod, "}")


with open("arquivo01.txt", "r") as arquivo:
    arquivo01 = arquivo.readlines()

with open("arquivo02.txt", "r") as arquivo2:
    arquivo02 = arquivo2.readlines()

with open("arquivo03.txt", "r") as arquivo3:
    arquivo03 = arquivo3.readlines()

print()


operacao(arquivo01)
print()

operacao(arquivo02)
print()

operacao(arquivo03)
print()




