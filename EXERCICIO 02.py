c1 = 0
c2 = 0 
c3 = 0
c4 = 0

print("Digite valores entre 0 e 100. Para encerrar, digite um número negativo.\n")
num = 0

while num >= 0:
    num = float(input("Digite um número: "))
  
    if num >= 0:
        if 0 <= num <= 25:
            c1 += 1
        elif 26 <= num <= 50:
            c2 += 1
        elif 51 <= num <= 75:
            c3 += 1
        elif 76 <= num <= 100:
            c4 += 1
          
print(f"\n[0-25]   : {c1} número(s)")
print(f"[26-50]  : {c2} número(s)")
print(f"[51-75]  : {c3} número(s)")
print(f"[76-100] : {c4} número(s)")
