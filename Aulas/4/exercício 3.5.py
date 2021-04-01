#Exercício 3.5
from numpy import * 

L1000 = [i for i in range(1000)]
y= [exp(0), exp(-5.e-5), exp(-1.e-4)] + L1000


u= y + [y[i+2]+(-5.e-5)*{(23/12)*y[i+2]-(4/3)*y[i+1]+(5/12)*y[i]} for i in L1000]