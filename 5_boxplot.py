#Boxplot = Diagrama de caixa

#import libs
import matplotlib.pyplot as plt
import random

#variaveis
vetor = []

#criando o vetor de 100 números com inteiros aletórios de 0 a 50
for i in range(100):
    num = random.randint(0,50)
    vetor.append(num)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
plt.savefig(r"graficos\boxplot.png", dpi = 300) #imagem em alta resolução