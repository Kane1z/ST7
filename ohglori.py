import random

# Variáveis globais
tabuleiro = ["_"] * 50
meta = 49
lista_negra = []
jogadores = None
#rodar dado
def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogada(posicao, jogador):
    if posicao == 3 or posicao == 8:
        posicao += 3
    elif posicao == 5:
        posicao = 0
    elif posicao == 16 or posicao == 35:
        print(f"Jogador {jogador} não poderá jogar na próxima rodada")
        lista_negra.append(jogador)
        return posicao
    elif posicao == 22:
        posicao += 2
    elif posicao == 27:
        posicao = jogadores[1] if len(jogadores) > 1 else posicao
        print("Sua posição agora é a mesma do Jogador 2!")
    elif posicao == 31:
        posicao += 1
    elif posicao == 38:
        posicao += 4
    elif posicao == 44 or posicao == 48:
        print(f"Jogador {jogador} voltou 4 posições atrás!")
        posicao -= 4
    return posicao

def showtab(jogadores):
    print("Tabuleiro dos Jogadores:")
    for i in range(len(jogadores)):
        visual = ["_" for _ in range(50)]
        if jogadores[i] <= meta:
            visual[jogadores[i]] = str(i + 1)
        print(f"Jogador {i + 1}: " + "".join(visual))

def escolha(min_jogadores, max_jogadores):
    while True:
        try:
            mx = int(input(f"Digite o número de jogadores (mínimo {min_jogadores}, máximo {max_jogadores}): "))
            if min_jogadores <= mx <= max_jogadores:
                return mx
            else:
                print(f"O número de jogadores deve ser entre {min_jogadores} e {max_jogadores}.")
        except ValueError: # uso de exept caso alguem coloque alcgo que nao seja 1 ou 4
            print("Por favor, insira um número válido.")


def start():
    mx = escolha(1, 4)
    jogadores = [0] * mx
    vez = 1
    showtab(jogadores)
    input("... qualquer tecla para começar com o jogador 1 ...\n")

    while True:
        if vez not in lista_negra:
            passo = dados()
            print(f"Jogador {vez} rolou os dados e tirou {passo}")
            nova_posicao = jogadores[vez - 1] + passo
            jogadores[vez - 1] = jogada(min(nova_posicao, meta), vez)
            print(f"Jogador {vez} está agora na posição {jogadores[vez - 1] + 1}")
            showtab(jogadores)
            input("... qualquer tecla para o próximo jogador ...\n")
        else:
            print(f"Jogador {vez} está revogado nesta rodada...\n")
            lista_negra.remove(vez)

        if jogadores[vez - 1] >= meta:
            print(f"Jogador {vez} venceu o jogo!")
            break
        vez += 1
        if vez > mx:
            vez = 1


