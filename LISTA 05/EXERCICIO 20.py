texto = input("Digite uma string: ")

inv = ""
i = len(texto) - 1

while i >= 0:
    inv += texto[i]
    i -= 1

print("String invertida:", inv)
