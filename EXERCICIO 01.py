divida_in = float(input("Digite o valor da dívida: R$ "))
print(f"\n{'Valor da Dívida':<17} {'Valor dos Juros':<17} {'Quantidade de Parcelas':<24} {'Valor da Parcela'}")
opcoes = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]
for parc, juros_pct in opcoes:
    juros = divida_in * (juros_pct / 100)
    divida_to = divida_in + juros
    valor_parc = divida_to / parc
    print(f"R$ {divida_to:<14.2f} {juros:<17.2f} {parc:<24} R$ {valor_parc:.2f}")
