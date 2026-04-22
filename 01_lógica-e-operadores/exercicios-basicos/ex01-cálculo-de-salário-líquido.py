salario_bruto = float(input("Digite o salário bruto: "))

desconto_inss = salario_bruto * 0.11
desconto_ir = salario_bruto *  0.15

salario_liquido = (salario_bruto - desconto_inss) - desconto_ir

print(f"O salário bruto é: R$ {salario_bruto:.3f}. Passou a ser R${salario_liquido:.3f} com todos os descontos")

