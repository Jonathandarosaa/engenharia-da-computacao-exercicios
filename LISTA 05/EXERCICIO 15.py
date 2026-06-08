matriz = [
    [12, 5, 8],
    [24, 67, 1],
    [9, 15, 3]
]

maior = matriz[0][0]
menor = matriz[0][0]

i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
        j += 1
    i += 1

print("Maior elemento:", maior)
print("Menor elemento:", menor)
