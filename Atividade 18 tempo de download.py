#Tempo de Download V1.0

print("Tempo de download")

var1 = input("Qual a velocidade da sua conexão (Mbps)? ")
conexao = float(var1)

mb =(conexao/8)
var2 = input("Informe o tamanho do arquivo (MB): ")
arquivo = float(var2)

tempo = arquivo/mb /60

print("Velocidade do download: {} Mbps".format(mb))
print('Tempo aproximado de download: {:.0f} Minutos '.format(tempo))