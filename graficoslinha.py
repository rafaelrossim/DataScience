#importacões de libs
import matplotlib.pyplot as plt

#variaveis
x = [1, 2, 5]
y = [3, 4, 7]

titulo = "Graficos em linhas"
eixox = "eixo X"
eixoy = "eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#utlizando o plot para criar graficos em linha
plt.plot(x, y)

#mostrando o grafico
plt.show()
