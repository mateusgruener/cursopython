# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:19:02 2021

@author: Usuario
"""
import funcoes

print("Hello World!")
############################################################################
print("\n")
#exemplos do livro:
    #comentários
    #continuação de linha\
print(2*3) #6
print(2**3) #8
print(2/3) #0.66666666666
#print(j**2)
############################################################################
print("\n")

a=3
b=4
if (a==b):
    print("a=b") #a identação é o que organiza os comandos
    print ("primeiro bloco")
else:
    print("a!=b")
    print("segundo bloco")
############################################################################
s="entre aspas" #string
print(s)

############################################################################
print("\n")
L = ['a', 2, [3, 4]] #lista
print(L[2])
h = len(L) #comprimento da lista
print(h)
L.append (3**80) #adicionar termo a lista
print(L[-1])

############################################################################
print("\nA LISTA L É")
#REPETIÇÃO
for i in L:
    print(i)
    print("foi 1 rodada")
print("acabou o loop")

###########################################################################
print("\n")
def f(x): #definindo funções
    f = 4*x**2 - 3*x + 8
    return f

print(f(2))

print("a função importada de 15 dá: ",funcoes.importada(15))
