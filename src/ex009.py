'''
    9. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
    vendedores com base em comissões. O vendedor recebe $200 por semana
    mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
    vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais
    9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando
    um array de contadores) que determine quantos vendedores receberam
    salários nos seguintes intervalos de valores:
    o $200 - $299
    o $300 - $399
    o $400 - $499
    o $500 - $599
    o $600 - $699
    o $700 - $799
    o $800 - $899
    o $900 - $999
    o $1000 em diante
    Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário,
    sem fazer vários ifs aninhados.
'''

# os vendedores serão definidos pelo usuário, seguindo a lógica da questão 8.

salarios = [[200, 299, 0], [300, 399, 0], [400, 499, 0], [500, 599, 0], [600, 699, 0], [700, 799, 0], [800, 899, 0],
            [900, 999, 0], [1000, 0]]
salario_fixo = 200
vendaBruta = vendedor = comissao = 0
print('Digite o valor da sua venda semanal: ')
print('Para sair do programa, digite "-1".\n')

while vendaBruta != -1:
    vendedor += 1
    vendaBruta = float(input(f'Vendedor {vendedor}: R$'))
    if vendaBruta == -1:
        break
    while vendaBruta <= -2:
        print('Valor inválido.')
        vendaBruta = float(input(f'Vendedor {vendedor}: R$'))
    comissao = vendaBruta * 9 / 100
    salario_vendedor = salario_fixo + comissao
    for index in range(0, len(salarios)):
        if int(salario_vendedor) >= salarios[len(salarios)-1][0]:
            salarios[len(salarios)-1][1] += 1
            break
        elif salarios[index][0] <= int(salario_vendedor) <= salarios[index][1]:
            salarios[index][2] += 1

print()
print('Você saiu do programa.\n')

for index in range(0, len(salarios)):
    if index < len(salarios)-1:
        print(f'No total, {salarios[index][2]} vendedores receberam o salário entre R${salarios[index][0]} a '
              f'R${salarios[index][1]}.')
    else:
        print(f'No total, {salarios[index][1]} vendedores receberam o salário maior do que R$1000.')
