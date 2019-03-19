'''#################################################################################
####    Nome: Matheus Peres                                                     ####
####    Programa: Listas e for                                                  ####
####    Data: 22-02-2019                                                        ####
#################################################################################'''

li = [1, 2]         #Criando a Lista

for x in li:        #for Iterado

    print(x)

for i in range(0,10):   #for comum

    print(i)

for i in range(0,10,2):   #for comum salto de 2

    print(i)

l1 = list(range(1,11))  #Criando uma lista con o range
print(l1)
print(l1[0:5])  #imprimindo os 5 primeiros itens da lista
print(l1[1:8])  #imprimindo a partir do 2 ao 9 iten da lista
print(l1[:5])   #imprimindo os 5 primeiros itens da lista
print(l1[5:10])  #imprimindo os 5 ultimos itens da lista
print(l1[0:10:2])  #imprimindo os itens da lista pulando 1
print(l1[::-1])  #imprimindo os itens da lista inversos
print(len(l1))  #Saber o tamanho da Lista
l1.reverse()    #inverte a lista
print(l1)

chaveValor = {'Matheus': 2 , 'Profeta': 3}
print(chaveValor)

for i in chaveValor:
    print(i)

for i in chaveValor.values():
    print(i)


tupla = (1,2,3,4,5,6)   #com uma tupla não consegue alterar
                        #o valor