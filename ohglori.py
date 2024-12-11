import random

# Configuração inicial
tabuleiro = list(range(50))
jogadores = {"Jogador 1": 0, "Jogador 2": 0, "Jogador 3": 0}
meta = 49

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def aplicar_regras(posicao):
    if posicao == 3 or posicao == 8:
        posicao += 3
    elif posicao == 5:
        posicao = 0
    elif posicao == 16 or posicao == 35:
        print("Você ficará sem jogar na próxima rodada!")
        return posicao, True
    elif posicao == 22:
        posicao += 2
    elif posicao == 27:
        posicao = jogadores["Jogador 2"]
        print("Sua posição agora é a mesma do Jogador 2!")
    elif posicao == 31:
        posicao += 1
    elif posicao == 38:
        posicao += 4
    elif posicao == 44 or posicao == 49:
        posicao -= 4
    return posicao,False

def jogar():
    rodada = 1
    while True:
        for jogador in jogadores:
            for i in tabo():
                print(" ".join(f"[{n:2}]" for n in i))
            print(f"\njogador {rodada} - {jogador} está na posição {jogadores[jogador]+1}")

            if jogadores[jogador] == meta:
                print(f"Parabéns! {jogador} venceu!")
                return


            input(f"{jogador}, pressione Enter para rolar os dados...")
            movimento = dados()
            print(f"{jogador} rolou {movimento}")
            jogadores[jogador] += movimento

            # aquiiiiiii verifixa se chegou no lvl max = meta = 49
            if (jogadores[jogador] > meta):
                jogadores[jogador] = meta - (jogadores[jogador] - meta)


            jogadores[jogador], pode_jogar = aplicar_regras(jogadores[jogador])
            if not pode_jogar:
                print(f"{jogador} não poderá jogar na próxima rodada.")

        rodada += 1

def tabo():
    tamanho = 7
    max_num = 49
    tabu = [[0] * 7 for i in range(tamanho)]
    x, y, dx, dy = 0, 0, 0, 1

    for num in range(1, max_num+1,1): # quando for 7 ele vira !!!
        tabu[x][y] = num
        if not (0 <= x + dx < tamanho and 0 <= y + dy < tamanho and tabu[x + dx][y + dy] == 0):
            dx, dy = dy, -dx
        x, y = x + dx, y + dy

    return tabu





jogar()