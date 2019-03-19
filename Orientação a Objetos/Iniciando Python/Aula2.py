print("Quem é voce?")

nome = input()

print("Qual e a sua idade?")

idade = int(input())

#Metodo 1

print("Ola {} sua idade é {}".format(nome,idade))

#Metodo 2

print('Ola ' + nome + ' sua idade é ' + str(idade))