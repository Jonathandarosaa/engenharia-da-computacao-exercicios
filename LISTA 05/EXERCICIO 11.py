n = int(input("Digite o número de termos (n): "))

soma = 0.0
num = 1
den = 1

print("S = ", end="")

while num <= n:
    soma += num / den
    
    if num == n:
        print(f"{num}/{den}")
    else:
        print(f"{num}/{den} + ", end="")
        
    num += 1
    den += 2

print(f"Soma total da série: {soma:.4f}")
