# Exibe uma solução do problema LocRSSF.
#
# Espera um arquivo que tenha as coordenadas X e Y (um nó por linha).
#
# O arquivo pode ser passado como argumento na linha de comando ou
# informado quando o programa é iniciado.
#
# @author Julio Cesar Alves
# @version 2016-12-08

import sys
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    nome_arq = sys.argv[1]
else:
    nome_arq = input("Nome do arquivo: ")
    
arq = open(nome_arq)

l_x = []
l_y = []
for linha in arq:
    x, y = map(float, linha.split())
    l_x.append(x)
    l_y.append(y)

plt.plot(l_x, l_y, "ro")
plt.show()

