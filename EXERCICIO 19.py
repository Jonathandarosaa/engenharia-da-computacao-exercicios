texto = input("Digite uma string: ")

v = 0
c = 0
i = 0

vogais = "aeiou"

while i < len(texto):
    letra = texto[i].lower()
    
    if letra.isalpha():
        if letra in vogais:
            v += 1
        else:
            c += 1
    i += 1

print("Vogais:", v)
print("Consoantes:", c)
