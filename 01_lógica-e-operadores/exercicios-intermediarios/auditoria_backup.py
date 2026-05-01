from datetime import datetime

num = input("Digite apenas o número do servidor (ex: 02): ")
tamanho_arquivo = float(input("Digie o tamanho do arquivo de backup (em GB): "))
data_backup = input("Digite a data do backup (DD/MM/YYYY): ")
data_today = input("Digite a data de hoje(DD/MM/YYYY): ")
servidor_final = ""
tentativas = 0


data_backup_formatada = datetime.strptime(data_backup, "%d/%m/%Y")
data_today_formatada = datetime.strptime(data_today, "%d/%m/%Y")

while tentativas < 3:
    
    if num.isdigit(): # Verifica se são apenas números
        servidor_final = f"servidor_{num}"
        print(f"Conectado ao: {servidor_final}")
        break
    else:
        tentativas += 1
        erro_restante = 3 - tentativas

        if erro_restante > 0:
            print("Erro: Digite apenas números!")
    
    if tentativas == 3:
        print("Acesso bloqueado. para desbloquear acesse o email em que enviamos para  j******ng@gmail.com")
    


if tamanho_arquivo == 0:
    print("O backup falhou, o arquivo de backup está vazio.")

elif tamanho_arquivo < 0.5 :
    print("O backup é muito pequeno.")

elif data_backup_formatada != data_today_formatada:
    
    print("ERRO: Backup desatualizado.")

else:
    print("Ok: backup realizado com sucesso.")
