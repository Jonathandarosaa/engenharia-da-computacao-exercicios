tot_l = 4
tot_c = 4

mat = []
i = 0

while i < tot_l:
    lin = []
    j = 0
    while j < tot_c:
        lin.append(i * j)
        j += 1
    mat.append(lin)
    i += 1

i = 0
while i < len(mat):
    print(mat[i])
    i += 1
