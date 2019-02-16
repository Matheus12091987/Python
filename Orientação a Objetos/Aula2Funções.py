def chamar_garcom():

    print('O garçom esta indo')
    print('Espere um pouco ...')

def cancela():

    print('Cancelando o pedido')
    print('Espere um pouco ...')

def fechar():

    print('Fechando sua conta')
    print('Espere um pouco ...')

def sair():

    print('Volte sempre')
    print('     !!     ')


print('--Menu--')
menu = '''
1 - Chamar o Garçon
2 - Cancelar o Pedido
3 - Fechar a conta
4 - Sair
'''

print(menu)

op = int(input())

operacoes = {   #Atribuir uma function a uma biblioteca
    1: chamar_garcom,
    2: cancela,
    3: fechar,
    4: sair
}

operacoes[op]() #Chamar a função atribuida

