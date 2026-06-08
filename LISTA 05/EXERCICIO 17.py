matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tot_l = len(matriz)
tam_ref = len(matriz[0])

eh_reg = True
i = 0

while i < tot_l:
    if len(matriz[i]) != tam_ref:
        eh_reg = False
    i += 1

res = eh_reg and (tot_l == tam_ref)

print(res)
