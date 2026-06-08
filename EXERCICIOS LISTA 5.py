# 01 -
divida_inicial = float(input("Digite o valor da dívida: R$ "))

print(f"\n{'Valor da Dívida':<17} {'Valor dos Juros':<17} {'Quantidade de Parcelas':<24} {'Valor da Parcela'}")


opcoes = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

for parcelas, juros_pct in opcoes:
    juros = divida_inicial * (juros_pct / 100)
    divida_total = divida_inicial + juros
    valor_parcela = divida_total / parcelas
    
    print(f"R$ {divida_total:<14.2f} {juros:<17.2f} {parcelas:<24} R$ {valor_parcela:.2f}")
