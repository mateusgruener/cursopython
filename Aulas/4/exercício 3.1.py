#Exercício 3.1
L = [1,2]
L3 = L*3

print ("L3 é ", L3)
print("L3[0] é ", L3[0]) #1
print("L3[-1] é ", L3[-1]) #2
#print("L3[10] é ", L3[10]) Out of range

L4 = [k**2 for k in L3]
print("L4 é ", L4)

L5 = L3 + L4
print("L5 é ", L5)