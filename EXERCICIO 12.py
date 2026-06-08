matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matriz)
s_p = 0
s_s = 0
i = 0

while i < n:
    s_p += matriz[i][i]
    s_s += matriz[i][n - 1 - i]
    i += 1

print("Soma da diagonal principal:", s_p)
print("Soma da diagonal secundaria:", s_s)
