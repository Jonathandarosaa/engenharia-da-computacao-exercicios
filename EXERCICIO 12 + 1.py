matriz = [
    [1, 2, 3],
    [4, 2, 6],
    [2, 8, 2]
]

alvo = 2
c = 0
i = 0

while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j] == alvo:
            c += 1
        j += 1
    i += 1

print(f"O elemento {alvo} aparece {c} vezes na matriz.")
