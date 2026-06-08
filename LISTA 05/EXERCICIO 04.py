v1 = 0
v2 = 0
v3 = 0
v4 = 0
nul = 0
brc = 0
tot = 0

voto = int(input("Digite o voto: "))
while voto != 0:
    if voto == 1:
        v1 += 1
        tot += 1
    elif voto == 2:
        v2 += 1
        tot += 1
    elif voto == 3:
        v3 += 1
        tot += 1
    elif voto == 4:
        v4 += 1
        tot += 1
    elif voto == 5:
        nul += 1
        tot += 1
    elif voto == 6:
        brc += 1
        tot += 1
    else:
        print("Voto inválido! Não será contabilizado.")
    voto = int(input("Digite o voto: "))
print("Candidato 1:", v1)
print("Candidato 2:", v2)
print("Candidato 3:", v3)
print("Candidato 4:", v4)
print("Nulos:", nul)
print("Brancos:", brc)
if tot > 0:
    print(f"Percentual nulos   : {(nul * 100 / tot):.2f}%")
    print(f"Percentual brancos : {(brc * 100 / tot):.2f}%")
