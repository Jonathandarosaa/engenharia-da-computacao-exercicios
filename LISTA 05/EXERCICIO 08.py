num = input("Digite um número inteiro positivo: ").strip()

if num.isdigit():
    inv = num[::-1]
    print(f"=> {inv}")
else:
    print("Por favor, digite apenas números inteiros e positivos.")
