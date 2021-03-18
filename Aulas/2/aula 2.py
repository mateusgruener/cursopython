def funcao(x):
    funcao= 2*x
    return funcao

a = input("Digite um número: ") #assim o programa lê como string

print(funcao(a))

b = int(input("Digite um número: ")) #agora ele lê como inteiro

print("o dobro de", b, "é",  funcao(b))