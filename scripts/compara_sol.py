# Compara duas soluções do problema LocRSSF.
#
# Espera dois arquivos que tenham as coordenadas X e Y (um nó por linha).
#
# Os arquivos podem ser passados como argumento na linha de comando ou
# informados quando o programa é iniciado.
#
# @author Julio Cesar Alves
# @version 2016-12-08

import sys

def ler_arq_solucao(nome_arq):
    arq = open(nome_arq)
    l = []
    for linha in arq:         
        l.append([float(x) for x in linha.split()])
    
    return l
    
def obter_nome_arq(indice, nome_padrao=""):
    if len(sys.argv) > indice:
        nome_arq = sys.argv[indice]
    elif nome_padrao == "":
        nome_arq = input("Nome do arquivo " + str(indice) + ": ")
    else:
        nome_arq = nome_padrao
    return nome_arq
  
def compara_dados(l1, l2):
    l = []
    if len(l1) != len(l2):
        print("ERRO: quantidade de dados diferentes")    
    for i in range(len(l1)):
        l.append([abs(l1[i][0] - l2[i][0]), abs(l1[i][1] - l2[i][1])])
    return l

def salvar_dados(l, nome_arq):
    arq_diff = open(nome_arq, "w")
    for e in l:
        #arq_diff.write(str(e[0]) + " " + str(e[1]) + "\n")
        arq_diff.write("{:.8f} {:.8f}\n".format(e[0], e[1]))


l1 = ler_arq_solucao(obter_nome_arq(1))
l2 = ler_arq_solucao(obter_nome_arq(2))

l_diff = compara_dados(l1,l2)
salvar_dados(l_diff, obter_nome_arq(3, "diff.txt"))
