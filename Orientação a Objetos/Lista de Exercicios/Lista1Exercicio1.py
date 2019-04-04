'''Exercicio 1 da Lista de Exercicios em Python'''

a = [1,1,2,3,5,8,13,21,34,55,89]

print("Resposta")
for i in a:
    if i < 5:
        print(i)

print("Resposta Extra 1")
x=[]
for i in a:
    if i < 5:
        x.append(i)
print(x)

print("Resposta Extra 2")
print (' '.join(str(x) for x in a if x < 5))

print("Resposta Extra 3")
valor = int(input("Digite um valor: "))
y=[]
for i in a:
    if i < valor:
        y.append(i)
print(y)