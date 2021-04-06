#exercício 4.7
from numpy import *
from matplotlib.pyplot import *
import scipy.linalg as sl

v=array([[1., -1., 1.]]).reshape(3,1)
print("v = ", v)
print("\n")
vT= v.reshape(1,3)
numerador = dot(v, vT)
denominador = dot(vT, v)

P=numerador/denominador
print ("P = ", P)
print("\n")

I = identity(3)
Q = I - P
print("Q = ", Q)
print("\n")

print(sl.eig(P))
print("\n")
print(sl.eig(Q))