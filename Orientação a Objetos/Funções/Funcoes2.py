def teste(n):

    for i in range(n+1):
        for j in range(i):
            print(i, end=" ")
        print("")

def teste2(n):
    for i in range(n+1):
        for j in range(i):
            print(j, end=" ")
        print("")

valor = int(input("Digite o numero de n: "))

teste(valor)
teste2(valor)