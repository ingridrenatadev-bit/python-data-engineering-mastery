valor_pago = float(input("valor pago no carro: "))
valor_investido = float(input("valor investido: "))
valor_venda = float(input("Valor da venda: "))

gasto = valor_pago + valor_investido
lucro = valor_venda - gasto

if lucro > 0:
    print(f"Você lucrou cerca de R${lucro:.4f} reais. Meus parabéns!!")
elif lucro < 0:
    print(f"Você obteve um prejuízo de R${lucro:.4f} reais. Deu ruim :(")
else:
    print("Empate")
