#Exercício 7.1

from matplotlib.pyplot import *
import numpy as np

def polar_to_comp(a, b):
    phic = b * 1j
    return a * np.exp(phic)

r = 1
phi = np.pi 
print (polar_to_comp(r, phi))