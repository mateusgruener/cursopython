#exercício 4.7
from numpy import *
from matplotlib.pyplot import *
import scipy.linalg as sl

v=array([[1., -1., 1.]]).T
print("v = ", v)
print("\n")
vT= v.T
numerador = dot(v, vT)
denominador = dot(vT, v)

P=numerador/denominador
print ("P = ", P)
print("\n")

I = identity(3)
Q = I - P
print("Q = ", Q)
print("\n")

print("P @ v = ", dot(P,v))
print("Portanto, o autovalor de P é 1\n")

print("Q @ v = ", dot(Q,v))
print("Portanto, o autovalor de Q é 0\n")
