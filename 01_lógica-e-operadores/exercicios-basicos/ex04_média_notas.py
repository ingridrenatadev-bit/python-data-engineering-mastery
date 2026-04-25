print("Olá, seja Bem-vindo ao Sistema de Média de Notas")

#página de login
print("Antes digite o seu nome e sua senha!")


#lista com nomes e senhas de funcionários que podem ter acesso ao sistema de notas
nomes_permitidos = ["Romário", "Lizandra", "Gregório", "Tauanny Oliveira"]
senhas_permitidas = ["romario123", "lizandra123", "gregorio321", "tauanny345"]

tentativas = 0


while tentativas < 3:
    nome = input("digite seu nome: ")
    senha = input("digite sua senha: ")

    if nome == nomes_permitidos and senha == senhas_permitidas:
        print(f"Seja Bem Vindo {nome}")
        
    else: 
        tentativas = tentativas + 1
        print(f"Senha errada. digite sua senha novamente {3 - tentativas} tentativas.")
if tentativas == 3:
        print("Perfil bloqueado. para desbloquear acesse o email em que enviamos para o email j******ng@gmail.com")
        


