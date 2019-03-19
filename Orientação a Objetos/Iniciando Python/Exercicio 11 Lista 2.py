'''#################################################################################
####    Nome: Matheus Peres                                                     ####
####    Programa: Exercicio 11 Estruturas Condicionais                          ####
####    Data: 22-02-2019                                                        ####
#################################################################################'''

salario_atual = float(input("Digite o Salario Atual: "))    '''Colocando o dado de 
                                                               entrada como float
                                                               o mesmo vem por
                                                               padrão STRING'''

taxa = .0

if salario_atual <= 280:
    taxa = .2
elif salario_atual <= 700:  #Else If em python fica simplificado a elif
    taxa = .15
elif salario_atual <= 1500:
    taxa = .1
else:
    taxa = .05

reajuste = salario_atual*taxa

print('O Salario atual: {}'.format(salario_atual))
print('Percentual {} % e reajuste: {}'.format(taxa*100,reajuste))
print('Novo Salario: {}'.format(salario_atual + reajuste))