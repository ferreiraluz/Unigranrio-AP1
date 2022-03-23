'''
    7. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
    número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
    ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
'''

from math import factorial


numero = int(input("Digite um número para ver sua tabuada: "))

for fator in range(0, 11):
    produto = numero * fator
    print("{} x {} = {}".format(numero, fator, produto))