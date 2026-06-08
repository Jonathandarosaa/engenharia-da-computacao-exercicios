n = int(input("Digite o número de termos (N): "))

h = 0.0
i = 1

while i <= n:
    h += 1 / i
    i += 1

print(f"Valor de H: {h:.4f}")
