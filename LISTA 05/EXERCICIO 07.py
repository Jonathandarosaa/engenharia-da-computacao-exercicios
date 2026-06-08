nome = input("Atleta: ").strip()

while nome != "":
    notas = []
    i = 0
    
    while i < 7:
        nt = float(input("Nota: "))
        notas.append(nt)
        i += 1
        
    melhor = max(notas)
    pior = min(notas)
    
    notas.remove(melhor)
    notas.remove(pior)
    
    med = sum(notas) / 5
    
    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {melhor:.1f}")
    print(f"Pior nota: {pior:.1f}")
    print(f"Média: {med:.2f}\n")
    
    nome = input("Atleta: ").strip()
