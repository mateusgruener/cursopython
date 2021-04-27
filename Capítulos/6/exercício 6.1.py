#exercício 6.1
from matplotlib.pyplot import *
import numpy as np

a=3
b=4

theta = np.linspace( -1 * np.pi, np.pi, 200)

x= a*np.cos(theta) + b*np.sin(theta)
y= -1 * a* np.sin(theta) + b*np.cos(theta)

plot(x,y, "r*")
show() 
