#Exercício 8.2
import numpy as np

print("a0=")
a = np.arange(2000)
a[0] = int(input())
n= int(input())
for i in range(3000):
    if(i<n):
        a[i+1] = 2*a[i]
    else:
        print(a[i])
        break
