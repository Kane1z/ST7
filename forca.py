import random
import string
def exibir_menu():
    print("esolhe um tema:")
    print("1 - Comidas(dificil)")
    print("2 - Países (medio)")
    print("3 - Marcas (facil)")
    print("-" * 25)

tema = -1
while tema != 0:
    exibir_menu()
    try:
        tema = int(input("Escolha o tema: "))
        if tema == 1:
            lista = ["Nugget", "Pizza", "Hambúrguer", "Kebab", "Espaguete", "Cola"]
            print("tema: Comidas")
            break
        elif tema == 2:
            lista = ["Portugal", "Brasil", "Austria", "Alemanha", "China", "Italia", "Angola"]
            print("tema: Países")
            break
        elif tema == 3:
            lista = ["Adidas", "Nike", "Bape", "Cropp", "PUMA", "McDonald's", "Lego"]
            print("tema: Marcas")
            break
        else:
            print("Opção inválida! Tente novamente.")
        print("-" * 25)

    except ValueError:
        print("tema invalido...")
        print("-" * 25)


palavra = lista[random.randint(0, len(lista)-1)]
palavra = palavra.lower()
#print(palavra) # palavra secreta ;)

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
    print('-' * 25)
    if char not in palavra and char != "":
        usado_errado.append(char)

    count = 0

    if char in usado and char != "":
        print("aviso: letra já usada")
    elif len(char) > 1:  # Verifica se a entrada tem mais de um caractere
        print("aviso: que palavrão")

    usado.append(char)
    for i in palavra:
        if i in usado:
            print(i + " ", end="")
            count += 1
        else:
            print("_ ", end="")
    print("")

    boneco(len(usado_errado))

    if len(usado_errado) > 0:
        print(f"{len(usado_errado)} erradas: " + '|'.join(usado_errado))  # print dos erros

    if count != len(palavra) and len(usado_errado) < 6:
        while True:
            next_char = input("char:").lower()
            if len(next_char) > 1:
                print("aviso: que palavrão")
            elif next_char in usado:
                print("aviso: letra já usada")
            elif next_char in string.digits:
                print("aviso: letra invalida")
            elif next_char.isalpha() == False:
                print("aviso: letra invalida")
            else:
                break
        printPal(next_char)

printPal("")