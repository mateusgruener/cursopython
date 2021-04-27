#exercício 7.4

import numpy as np

def bisec(f, a, b, tolerancia):
    def f(x):
        return f
    if {b - a < tolerancia}:
        return [[a , b] , [(a+b)/2]]
    elif (f(a)*f(a+b/2) < 0):
        b = (a + b)/2
    elif (f((a+b)/2)*f(b) < 0):
        a = (a + b)/2
        
print (bisec(np.arctan, 1.1, 1.4, 1e-10 ))