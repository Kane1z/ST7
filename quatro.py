# Código atualizado 21/10/24 -- 23:32
tabuleiro = [[' ' for i in range(6)] for j in range(6)]
turno = 1
ini = True

while ini == True:
    for linha in range(len(tabuleiro)):
        for coluna in range(6):
            if (linha == 0):
                print('|', coluna + 1, '', end='')
            else:
                print('|', tabuleiro[linha][coluna], '', end='')
        print('|')
    print('-' * 25)
    # Código atualizado 22/10/24 -- 21:32 (atualizacao de turno)
    if (turno == 1):
        print("turno 1")
        coluna = int(input("Escolha uma coluna (1-6): ")) - 1
        char = 'X'
    else:
        print("turno 2")
        coluna = int(input("Escolha uma coluna (1-6): ")) - 1
        char = 'O'

    '''colocquei esse for que comeca na linha 5 ate 
          o final para verificar se há algo em baixo gostei bastante parece uma cascata'''
    if (coluna >= 0 and coluna <= 6):
        inserido = False
        for linha in range(5, 0, -1):
            if (tabuleiro[linha][coluna] == ' '):
                tabuleiro[linha][coluna] = char
                inserido = True
                break
        if (inserido == False):
            print("Coluna cheia, escolha outra.")
        else:
            '''caso nao esteja cheia vai 
                ficar vareando entre turno 1 e 2'''
            if (turno == 1):
                turno = 2
            else:
                turno = 1
            # Código atualizado 23/10/24 -- 00:18 (atualizacao de verificacao de vencer)
            combobraker = 0
            '''muito basico vai fazer 2 verificacoes talvez ahaja repeticao de codigo mas... eh'''
            # Buffer overflow: quando o código decide que é hora de dar uma pausa mas eu não.
            for i in range(6):  # vericao horizontal
                if (tabuleiro[linha][i] == char):
                    combobraker += 1
                    if (combobraker == 4):
                        ini = False
                        if (char == 'X'):
                            print("Jogador 1 venceu yay!")
                        else:
                            print("Jogador 2 venceu yay!")
                        break
                else:
                    combobraker = 0
            if (ini == False):
                break

            combobraker = 0
            for i in range(6):  # verificacao vertical
                if (tabuleiro[i][coluna] == char):
                    combobraker += 1
                    if (combobraker == 4):
                        ini = False
                        if (char == 'X'):
                            print("Jogador 1 venceu!")
                        else:
                            print("Jogador 2 venceu!")
                        break
                else:
                    combobraker = 0
    else:
        print("Coluna não existe!")

