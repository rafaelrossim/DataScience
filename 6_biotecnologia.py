"""
DNA é uma molécula presente em todos os seres vivos, que é responsável por armazenar as características hereditárias. Ela é composta por sequências de nucleotídeos, que podem de quatro tipos: adenina, timina, citosina ou guanina.

"Computacionalmente" falando podemos representá-los através de 4 letras: A, T, C ou G.

Neste estudo de caso, queremos avaliar se estruturas com funções parecidas (estamos usando sequências de RNA ribossomal) de organismos diferentes têm diferenças. Para isso vamos avaliar a quantidade de pares de nucleotídeos.

"""

#lendo arquivos
from itertools import count


entrada = open(r"data\biotecnologia\bacteria.fasta").read()
saida = open(r"html\bacteria.html", "w")

cont = {}

#populando o dicionário(cont) com todas as possibildades de pares de nucleotídeos, iniciando com a contagem de pares em 0
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

#tratando quebra de linha no arquivo
entrada = entrada.replace("\n","")

#contando os pares de nucleotídeos
for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

#html
i = 1

#criando html com os resultados
for k in cont:
    transp = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; color: #fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transp)+"')>"+k+"</div>")

    #quebra de linha a cada quatro quadrados
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    i+=1

saida.close()