matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

inv = []
i = len(matriz) - 1

while i >= 0:
    inv.append(matriz[i])
    i -= 1

i = 0
while i < len(inv):
    print(inv[i])
    i += 1
