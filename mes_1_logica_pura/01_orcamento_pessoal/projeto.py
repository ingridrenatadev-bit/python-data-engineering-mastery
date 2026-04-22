print("=====CONTROLADORIA DE ORÇAMENTO PESSOAL=====")

receita_total = float(input("Insira o valor da sua receita (R$): "))
total_despesas = float(input("Insira o valor total das suas despesas mensais (R$): "))

lucro = receita_total - total_despesas
percentual_despesa = (total_despesas /receita_total) * 100    

if lucro > 0:
    print(f"\n Você teve LUCRO de R$ {lucro:.2f}")
elif lucro == 0:
    print(f"\n Você EMPATOU (receita = despesas)")
else:
    print(f"\n Você teve PREJUÍZO de R$ {(lucro):.2f}")

print(f"Despesas representam {percentual_despesa:.1f}% da receita")
