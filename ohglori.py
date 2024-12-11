import random

# Configuração inicial
tabuleiro = list(range(50))
jogadores = [0,0,0,0]
meta = 49
lista_negra = []
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
        print(f"Jogador{jogador} não podera jogar na proxima partida")
        lista_negra.append(jogador)
        return False
    elif posicao == 22:
        posicao += 2
    elif posicao == 27:
        posicao = jogadores[1]
        print("Sua posição agora é a mesma do Jogador 2!")
    elif posicao == 31:
        posicao += 1
    elif posicao == 38:
        posicao += 4
    elif posicao == 44 or posicao == 49:
        print(f"Jogador{jogador} voltou 4 posicoes atrás!")
        posicao -= 4
    return posicao

mx = int(input("maximo de jogadores: "))
vez = 1

while True:
    print(lista_negra)
    passo = dados()
    jogadores[vez-1] = jogadores[vez-1] + passo
    if (vez not in lista_negra):
        print(f"Jogador{vez} está em {jogada(jogadores[vez-1],vez)}")
        vez += 1
        input("... qualquer tecla pra proximo jogador ...")
        print("")
    else:
        print(f"jogador{vez} revogado...")
        lista_negra.remove(vez)
        vez += 1
    if vez > mx:
        vez = 1
