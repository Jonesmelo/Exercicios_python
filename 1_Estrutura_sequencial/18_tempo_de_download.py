#Atividade 18
# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Velocidade de download v2.0
# Criado por Jones Melo

print("Velocidade de Download\n")
print("Insira 0 para sair do programa")


while 1: #Loop quase infinito, para repitir uma nova consulta   
    var1 = input("Qual a velocidade da sua conexão (Mbps)? ") #Interação com o usuario
    conexao = float(var1)

    mb =(conexao/8) #Converte a velocidade 
    var2 = input("Informe o tamanho do arquivo (MB): ")
    arquivo = float(var2)

    if conexao == 0 or arquivo == 0: #Caso o usuario digite 0 em alguma das pertuntas, o programa será encerrado 
        print("Programa encerrado")
        break #Parar laço

    else:
        tempo = arquivo/mb /60 #tempo de download

        print("Velocidade do download: {} Mbps".format(mb))
        print('Tempo aproximado de download: {:.0f} Minutos '.format(tempo))
        print("")
        print("Nova consulta")