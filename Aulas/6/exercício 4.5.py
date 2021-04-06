from numpy import *
from matplotlib.pyplot import *
import scipy.linalg as sl


#exercício 4.5

x= (0.0, 0.5, 1.0, 1.5, 2.0, 2.5)

V= array([[x[0]**5, x[0]**4, x[0]**3, x[0]**2, x[0]**1, x[0]**0],
          [x[1]**5, x[1]**4, x[1]**3, x[1]**2, x[1]**1, x[1]**0],
          [x[2]**5, x[2]**4, x[2]**3, x[2]**2, x[2]**1, x[2]**0],
          [x[3]**5, x[3]**4, x[3]**3, x[3]**2, x[3]**1, x[3]**0],
          [x[4]**5, x[4]**4, x[4]**3, x[4]**2, x[4]**1, x[4]**0],
          [x[5]**5, x[5]**4, x[5]**3, x[5]**2, x[5]**1, x[5]**0]])

print("V = ", V)
print("\n")
A = V[:,1:]

print ("A = ", A)
print("\n")
AT=A.T
B = sl.inv(dot(AT, A))@AT

print("B = ", B)
print("\n")

y= (-2.0, 0.5, -2.0, 1.0, -0.5, 1.0)

c = dot(B, y)

print("c = ", c)
print("\n")

