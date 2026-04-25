peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

print(f"Seu IMC é de {imc:.1f}")

if imc <= 22:
    print("Baixo peso!")
elif imc > 22 and imc <= 27:
    print("Peso adequado!")
elif imc > 27 and imc <=29.9:
    print("Sobre peso")
else:
    print("Obesidade morbida, procure um médico!")


