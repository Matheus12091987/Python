class Pessoa:

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getIdade(self):
        return self.idade

    #Sobreposição Polimorfismo __str__ é uma função interna do Python
    #quando faz esta função abaixo ele modificou a função original
    #para esta função abaixo
    def __str__(self):
        return f'Modificado {self.nome} {self.idade}'

    #Construtor
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

class PessoaFisica(Pessoa):

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

    def __str__(self):
        return f'{super().__str__()} {self.cpf}'
#_____________________________________________________________

obj = Pessoa()
obj.nome = "Fabricio"
obj.idade = 32

obj2 = Pessoa("Luiza", 2)

print(f'O meu nome é {obj.getNome()} e idade {obj.idade}')
print(f'O meu nome é {obj.nome} e idade {obj.idade}')
print(obj)
print(obj2)

obj3 = PessoaFisica()
obj3.setNome("Rodrigo")
obj3.setIdade(50)
obj3.setCpf(34653763828)

print(obj3)