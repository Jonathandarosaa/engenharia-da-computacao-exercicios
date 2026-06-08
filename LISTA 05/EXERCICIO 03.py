print("--- CARDÁPIO LANCHONETE ---")
print("100 - Cachorro Quente : R$ 1,20")
print("101 - Bauru Simples   : R$ 1,30")
print("102 - Bauru com ovo   : R$ 1,50")
print("103 - Hambúrguer      : R$ 1,20")
print("104 - Cheeseburguer   : R$ 1,30")
print("105 - Refrigerante    : R$ 1,00")
print("0   - Encerrar Pedido\n")

tot = 0 
cod = int(input("Digite o código do produto ou 0 para sair: "))
while cod != 0:
    if cod == 100:
        prc = 1.20
    elif cod == 101:
        prc = 1.30
    elif cod == 102:
        prc = 1.50
    elif cod == 103:
        prc = 1.20
    elif cod == 104:
        prc = 1.30
    elif cod == 105:
        prc = 1.00
    else:
        prc = -1
        print("Código inválido!")
    if prc > 0:
        qtd = int(input("Digite a quantidade: "))
        val = prc * qtd 
        tot += val
        print(f"Valor do item: R$ {val:.2f}\n")
    cod = int(input("Digite o código do produto ou 0 para sair: "))
print(f"\nTotal do pedido: R$ {tot:.2f}")
