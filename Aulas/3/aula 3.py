import sys
a = sys.float_info.epsilon #o valor de um intervalo numérico infinitesimal no meu computador
print(a)
#______________________________________________________________________________________
print("\n")

print (1j**2) #j é o número complexo #retorna -1+0j
print ((1j**2).real) #retorna -1.0
print (int((1j**2).real)) #retorna -1

#______________________________________________________________________________________
print("\n")

print("a\tb\tc\td") #\t = 8 espaços

#______________________________________________________________________________________
print("\n")

sequencia='abcdeaaabcd'
print(sequencia.find('a')) #retorna a posição onde é encontrado o caractere informado
#______________________________________________________________________________________
print("\n")

a=6
print(a)
print("{:f}".format(a))