from datetime import datetime
import sys

num = input("Digite apenas o número do servidor (ex: 02): ")
tentativas = 0

#-------------- Bloco para validar o número do servidor --------------

while tentativas < 3: #verifica se o número do servidor é válido, caso contrário, bloqueia o acesso após 3 tentativas
    
    if num.isdigit(): # Verifica se são apenas números
        servidor_final = f"servidor_{num}"
        print(f"Conectado ao: {servidor_final}")
        break
    else:
        tentativas = tentativas + 1
        erro_restante = 3 - tentativas

        if erro_restante > 1:
            print(f"Erro: Digite apenas números! {erro_restante} tentativas restantes.")
    
            if erro_restante == 3:
                print("Acesso bloqueado. para desbloquear acesse o email em que enviamos para  j******ng@gmail.com")
                sys.exit()

#-------------- Bloco para validar o tamanho do arquivo de backup --------------
while True: #

    tamanho_arquivo = input("Digite o tamanho do arquivo de backup (em GB): ").replace(",", ".")   

    try:
        tamanho_float = float(tamanho_arquivo)

        if tamanho_float < 0.5 or tamanho_float == 0 :
            print("O backup é muito pequeno.")        
            break

    except ValueError:
        print("Erro: Digite um número válido para o tamanho do arquivo de backup.")

#-------------- Bloco para validar as datas --------------

while True:
    data_backup = input("Digite a data do backup (DD/MM/YYYY): ")
    data_today = input("Digite a data de hoje(DD/MM/YYYY): ")
    
    try:
        data_backup_formatada = datetime.strptime(data_backup, "%d/%m/%Y")
        data_today_formatada = datetime.strptime(data_today, "%d/%m/%Y")

        if data_backup_formatada == data_today_formatada:
            print(f"Os backups são de hoje. Data: {data_today_formatada}")
            break
    
    except ValueError:
        print("Erro: As datas não estão corretas ou não é backup de hoje.")

print(f"\n Servidor: {servidor_final} \n Data: {data_backup_formatada} \n Tamanho: {tamanho_float} GB \n Status: OK")

    






    

