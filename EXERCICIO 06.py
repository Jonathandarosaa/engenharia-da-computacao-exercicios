nome = input("Atleta: ").strip()

while nome != "":
    saltos = []
    ordem = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    i = 0
    
    while i < 5:
        s = float(input(f"{ordem[i]} Salto: "))
        saltos.append(s)
        i += 1
        
    melhor = max(saltos)
    pior = min(saltos)
    
    saltos.remove(melhor)
    saltos.remove(pior)
    
    med = sum(saltos) / 3
    
    print(f"\nMelhor salto: {melhor:.1f} m")
    print(f"Pior salto: {pior:.1f} m")
    print(f"Média dos demais saltos: {med:.1f} m")
    print("\nResultado final:")
    print(f"{nome}: {med:.1f} m\n")
    
    nome = input("Atleta: ").strip()
