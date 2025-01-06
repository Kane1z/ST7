import galo, quatro, ohglori, forca
def exibir_menu():
    print("esolhe um jogo:")
    print("1 - jogo do galo")
    print("2 - jogo do 4 em linha")
    print("3 - jogo da gloria")
    print("4 - jogo da forca")
    print("-" * 25)

jogo = -1
while jogo != 0:
    exibir_menu()
    try:
        jogo = int(input("Escolha o jogo: "))
        if jogo == 1:
            galo.start(" ")
            break
        elif jogo == 2:
            quatro.start()
            break
        elif jogo == 3:
            ohglori.start()
            break
        elif jogo == 4:
            forca.start()
            break
        else:
            print("Opção inválida! Tente novamente.")
        print("-" * 25)

    except ValueError:
        print("jogo n existe :\\")
        print("-" * 25)
print("-" * 25)