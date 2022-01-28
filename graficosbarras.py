#importacões de libs
import matplotlib.pyplot as plt

#variaveis
x=[1, 2, 3, 4, 5]
y=[3, 4, 7, 1, 0]
titulo = "Graficos em barras"
eixox = "eixo X"
eixoy = "eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#utlizando o bar para criar graficos em barras
plt.bar(x, y)

#mostrando o grafico
plt.show()
