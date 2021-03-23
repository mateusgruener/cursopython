#atividades aula 3

#1 .  Check whether x = 2.3 is a zero of the function...

def f(x):
    f= x**2 + 0.25 * x - 5 
    return f

if (f(2.3)==0):
    print("2.3 é uma raiz da função definida.")
else:
    print("2.3 não é uma raiz da função definida.")

print("f(2.3) = ", f(2.3))
