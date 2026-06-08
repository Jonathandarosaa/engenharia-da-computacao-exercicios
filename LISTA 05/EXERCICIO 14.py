matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

lin = len(matriz)
col = len(matriz[0])

trans = []
j = 0

while j < col:
    nova_lin = []
    i = 0
    while i < lin:
        nova_lin.append(matriz[i][j])
        i += 1
    trans.append(nova_lin)
    j += 1

i = 0
while i < len(trans):
    print(trans[i])
    i += 1
