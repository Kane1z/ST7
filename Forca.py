import random
from traceback import print_tb

lista = ["nugget","pizza","hamburger","kebab"]
palavra = lista[random.randint(0, len(lista)-1)]

#print(palavra)

venceu = True
usado = []
usado_errado = []

def boneco(lvl):
    print(" _______")        # Barra horizontal superior
    print(" |     |")       # Suporte vertical
    if lvl >= 1:            # Cabeça
        print(" |     0 ")
    else:
        print(" |")
    if lvl == 2:            # Corpo
        print(" |     | ")
    elif lvl == 3:          # Corpo + Braço esquerdo
        print(" |    /| ")
    elif lvl >= 4:          # Corpo + Ambos os braços
        print(" |    /|\\")
    else:
        print(" |")
    if lvl == 5:            # Uma perna
        print(" |    /  ")
    elif lvl >= 6:          # Ambas as pernas
        print(" |    / \\")
    else:
        print(" |")
    print(" |")             # Final do suporte
    print("_|_")            # Base



def printPal(char):
    if char not in palavra:
        usado_errado.append(char)


    count = 0
    usado.append(char)
    for i in palavra:
        if i in usado:
            print(i+ " ", end="")
            count+=1
        else:
            print("_ ", end="")
    print("")
    boneco(len(usado_errado))

    if count !=len(palavra) and len(usado_errado) < 6:
        printPal(input("char:"))


printPal("")

