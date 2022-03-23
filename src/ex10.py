'''
    10.Faça um programa que use a função valorPagamento para determinar o valor
    a ser pago por uma prestação de uma conta. O programa deverá solicitar ao
    usuário o valor da prestação e o número de dias em atraso e passar estes
    valores para a função valorPagamento, que calculará o valor a ser pago e
    devolverá este valor ao programa que a chamou. O programa deverá então
    exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a
    pedir outro valor de prestação e assim continuar até que seja informado um
    valor igual a zero para a prestação. Neste momento o programa deverá ser
    encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
    de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
    forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando
    houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(prestacao, atraso):
    if atraso == 0:
        return prestacao
    else:
        return prestacao + (prestacao * 3 / 100) + (prestacao * 0.1 / 100) * atraso


print('Digite o valor da prestação e a quantidade de dias em atraso para calcular o valor total a ser pago.')
print('Para sair do programa, digite "0" no valor da prestação.')
print()
valorPrestacao = diasAtrasados = prestacao = totalPrestacao = 0

while True:
    valorPrestacao = float(input('Valor da prestação: R$'))
    if valorPrestacao == 0:
        print('Você saiu do programa.\n')
        break
    while valorPrestacao < 0:
        print('Valor inválido.')
        valorPrestacao = float(input('Valor da prestação: R$'))
    diasAtrasados = int(input('Dias em atraso: '))
    prestacao += 1
    totalaAPagarPrestacao = valorPagamento(valorPrestacao, diasAtrasados)
    totalPrestacao +=totalaAPagarPrestacao
    print(f'O valor a ser pago é de R${totalaAPagarPrestacao:.2f}.')
    print()

print(f'No dia de hoje, foram pagas {prestacao} prestações, somando o valor total de R${totalPrestacao:.2f}.')