def tabu():
    return [[' ' for i in range(6)] for j in range(6)]

def imprimir_tabuleiro(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(6):
            if linha == 0:
                print('|', coluna + 1, '', end='')
            else:
                print('|', tabuleiro[linha][coluna], '', end='')
        print('|')
    print('-' * 25)

def inserir_peca(tabuleiro, coluna, char):
    for linha in range(5, 0, -1):
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = char
            return linha, True
    return -1, False

def verificar_vitoria(tabuleiro, linha, coluna, char):
    def contar_sequencia(delta_l, delta_c):
        contador = 0
        for passo in range(-3, 4):
            l, c = linha + passo * delta_l, coluna + passo * delta_c
            if 0 <= l < 6 and 0 <= c < 6 and tabuleiro[l][c] == char:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0
        return False

    return (contar_sequencia(0, 1) or  # Horizontal
            contar_sequencia(1, 0) or  # Vertical
            contar_sequencia(1, 1) or  # Diagonal \
            contar_sequencia(1, -1))   # Diagonal /

def trocar_turno(turno):
    return 2 if turno == 1 else 1

def start():
    tabuleiro = tabu() #futuramnete guradar tabuleiro em txt e ler
    turno = 1
    ini = True

    while ini:
        imprimir_tabuleiro(tabuleiro)

        char = 'X' if turno == 1 else 'O'
        print(f"Turno {turno}")

        try:
            coluna = int(input("Escolha uma coluna (1-6): ")) - 1
            if not (0 <= coluna < 6):
                raise ValueError
        except ValueError:
            print("Coluna inválida! Tente novamente.")
            continue

        linha, inserido = inserir_peca(tabuleiro, coluna, char)
        if not inserido:
            print("Coluna cheia, escolha outra.")
            continue

        if verificar_vitoria(tabuleiro, linha, coluna, char):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {turno} venceu! Parabéns!")
            ini = False
        else:
            turno = trocar_turno(turno)
