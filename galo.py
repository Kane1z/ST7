


def tabu():
    return [[' ' for i in range(3)] for j in range(3)]

def mostra(tabuleiro):
    print("")
    for i in range(3):
        print(tabuleiro[i][0], '|', tabuleiro[i][1], '|', tabuleiro[i][2])
        print('-' * 10)

def verificar_vencedor(tabuleiro):
    # Verificação horizontal
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1]) and (tabuleiro[i][1] == tabuleiro[i][2]) and (tabuleiro[i][0] != ' '):
            return tabuleiro[i][0]

    # Verificação vertical
    for i in range(3):
        if (tabuleiro[0][i] == tabuleiro[1][i]) and (tabuleiro[1][i] == tabuleiro[2][i]) and (tabuleiro[0][i] != ' '):
            return tabuleiro[0][i]

    # Verificação diagonal
    if (tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2]) and (tabuleiro[0][0] != ' '):
        return tabuleiro[0][0]
    if (tabuleiro[0][2] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][0]) and (tabuleiro[0][2] != ' '):
        return tabuleiro[0][2]

    return None

def jogada_valida(tabuleiro, x, y):
    return tabuleiro[y][x] == ' '

def atualizar_tabuleiro(tabuleiro, x, y, jogador):
    tabuleiro[y][x] = 'X' if jogador == 1 else 'O'

# Jogo principal
def start(tabuleiro):
    if tabuleiro != "":
        tabuleiro = tabu()
    rondas = 0
    jogador = 1
    vencedor = None

    while rondas < 9 and not vencedor:
        mostra(tabuleiro)
        print("Jogador", jogador)

        try:
            y = int(input("linha: ")) - 1
            x = int(input("coluna: ")) - 1
            if 0 <= x < 3 and 0 <= y < 3:
                if jogada_valida(tabuleiro, x, y):
                    atualizar_tabuleiro(tabuleiro, x, y, jogador)
                    jogador = 3 - jogador
                    rondas += 1
                    vencedor = verificar_vencedor(tabuleiro)
                else:
                    print("Posição já ocupada!")
            else:
                print("Entrada inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Use apenas números.")

        if vencedor == 'X':
            print("Jogador 1 'X' venceu!")
        elif vencedor == 'O':
            print("Jogador 2 'O' venceu!")

    mostra(tabuleiro)
    if not vencedor:
        print("Fim do jogo! Empate!")


