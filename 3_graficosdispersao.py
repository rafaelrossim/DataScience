#importacões de libs
from cProfile import label
import matplotlib.pyplot as plt

#variaveis
x = [1, 2, 3, 4, 5]
y = [3, 4, 7, 2, 4]

titulo = "Graficos Dispersão (Pontos)"
eixox = "eixo X"
eixoy = "eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#utlizando o scatter e plot para criar graficos ligando os pontos (despersão)
plt.plot(x, y, color = "k")
plt.scatter(x, y, color = "r", label = "Meus pontos") #o atributo "color" pode usar também valores hexadecimais
plt.legend()

#mostrando o grafico
plt.show()

#salvando o grafico
plt.savefig(r"graficos\grafico_pontos.png", dpi = 300) #imagem em alta resolução
plt.savefig(r"graficos\grafico_pontos.pdf")

"""
Documentação oficial do Matplotlib
A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).

color: cor (ver exemplos abaixo)
label: rótulo
linestyle: estilo de linha (ver exemplos abaixo)
linewidth: largura da linha
marker: marcador (ver exemplos abaixo)

CORES (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

Marcadores (marker)
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker=
's' square marker
'p' pentagon marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker

Tipos de linha (linestyle)
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style
"""
