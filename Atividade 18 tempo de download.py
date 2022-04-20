#Velocidade do download v2.0
#Criado por Jones Melo

print("Downloading...")


while 1:    
    var1 = input("Qual a velocidade da sua conexão (Mbps)? ")
    conexao = float(var1)

    mb =(conexao/8)
    var2 = input("Informe o tamanho do arquivo (MB): ")
    arquivo = float(var2)

    if conexao == 0 or arquivo == 0:
        print("Programa encerrado")
        break

    else:
        tempo = arquivo/mb /60

        print("Velocidade do download: {} Mbps".format(mb))
        print('Tempo aproximado de download: {:.0f} Minutos '.format(tempo))
        print("")
        print("Nova consulta")