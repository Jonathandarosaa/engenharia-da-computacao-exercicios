gab = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

maior = -1
menor = 11
tot_al = 0
soma_nt = 0

resp_sistema = "S"

while resp_sistema == "S":
    acertos = 0
    i = 0
    
    while i < 10:
        resp = input(f"Resposta da questao {i + 1}: ").strip().upper()
        if resp == gab[i]:
            acertos += 1
        i += 1
        
    print("Total de acertos:", acertos)
    
    if acertos > maior:
        maior = acertos
    if acertos < menor:
        menor = acertos
        
    tot_al += 1
    soma_nt += acertos
    
    resp_sistema = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()

print("Maior acerto:", maior)
print("Menor acerto:", menor)
print("Total de alunos:", tot_al)

if tot_al > 0:
    med = soma_nt / tot_al
    print("Media da turma:", med)
