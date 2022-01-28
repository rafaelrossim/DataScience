#importacões de libs
import matplotlib.pyplot as plt

#variaveis
x1 = [1, 2, 3, 4, 5]
y1 = [3, 4, 7, 2, 4]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 8, 4, 4]

titulo = "Graficos em barras"
eixox = "eixo X"
eixoy = "eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#utlizando o bar para criar graficos em barras
plt.bar(x1, y1, label = "Grupo 1") # colocando a legenda das cores
plt.bar(x2, y2, label = "Grupo 1")
plt.legend() #mostrando a leganda no gráfico

#mostrando o grafico
plt.show()
