#Crescimento da população Brasileira dos anos de 1980 a 2016

#import libs
import matplotlib.pyplot as plt

#variaveis
dados = open("data\populacao_brasileira.csv").readlines()
x = [] #ano
y = [] #populacao

#lendo e tratando os dados
for i in range(len(dados)):
    if i != 0: #igorar o header do csv
        linha = dados[i].split(";") #splitando por ponto e virgual
        x.append(int(linha[0]))
        y.append(int(linha[1]))

#legendas
plt.title("Crescimento da população Brasileira dos anos de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")

#criando grafico
plt.bar(x,y, color = "#e4e4e4")
plt.plot(x,y)

#mostrando/salvando o grafico
plt.show()
plt.savefig(r"graficos\populacao_brasileria.jpg", dpi = 300)
