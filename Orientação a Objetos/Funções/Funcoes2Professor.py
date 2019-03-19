def mensagem(n):

	for i in range(1, n+1):

	    print('{} '.format(i)*i)

def mensagem2(n):

    for i in range(1, n+1):

	    print(' '.join([str(x) for x in range (1,i+1)]))

def main():
    m = int(input('Digite um numero qualquer: '))
    mensagem(m)
    mensagem2(m)

if __name__ == '__main__':

    main()