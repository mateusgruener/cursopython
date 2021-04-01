#exercício 3.3

L = [0,1,2,1,0,-1,-2,-1,0]
L[0] #primeiro elemento da lista
L[-1] #último elemento da lista
L[:-1] #lista toda sem o último elemento
L + L[1:-1] + L #concatena a lista toda, a lista sem os extremos e a lista toda de novo
L[2:2] = [-3] #insere -3 na posição 3
L[3:4] = [] #tira o 4º elemento
L[2:5] = [-5] #tira os elementos 2, 3 e 4 e substitui por [-5] (um só)


