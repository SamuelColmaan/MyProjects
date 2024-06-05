try:
    n1 = int(input('Informe um número inteiro:'))
    if n1 % 2 == 0:
        print('Esse número é par')
    elif n1 % 2 != 0:
        print('Esse número é ímpar')
except ValueError:
    print('Você não digitou um número inteiro')