from tokenize import PlainToken
#importacões de libs
import matplotlib.pyplot as plt

#criando valores dos eixos
x=[1,2,5]
y=[3,4,7]

#criando titulo do grafico
plt.title("Grafico em linhas")

#criando legenda dos eixos
plt.xlabel("Eixo x")
plt.ylabel("Eixo Y")

#utlizando o plot para criar graficos em linha
plt.plot(x, y)

#mostrando o grafico
plt.show()

