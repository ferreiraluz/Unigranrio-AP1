'''
    
    6. As Organizações Tabajara resolveram dar um aumento de salário aos seus
    colaboradores e lhe contrataram para desenvolver o programa que calculará os
    reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste
    segundo o seguinte critério, baseado no salário atual:
    o salários até R$ 280,00 (incluindo) : aumento de 20%
    o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    o salários de R$ 1500,00 em diante : aumento de 5%.
     
    Após o aumento ser
    realizado, informe na tela:
    o o salário antes do reajuste;
    o o percentual de aumento aplicado;
    o o valor do aumento;
    o o novo salário, após o aumento.
'''

salario = float(input("Digite seu salário: "))

if(salario <= 280.0):
    porcentagem = "20%"
    aumento = (salario * 20)/100
    salarioNovo = salario + aumento
elif(salario > 280.0 and salario <= 700.0):
    porcentagem = "15%"
    aumento = (salario * 15)/100
    salarioNovo = salario + aumento
elif(salario > 700.0 and salario <= 1500):
    porcentagem = "10%"
    aumento = (salario * 10)/100
    salarioNovo = salario + aumento
elif(salario > 1500):
    porcentagem = "5%"
    aumento = (salario * 5)/100
    salarioNovo = salario + aumento

print("Seu salário antes do reajuste era {}. Seu percentual de aumento foi de {}. O valor do aumento foi de {}. E o seu novo salário é {}.".format(salario, porcentagem, aumento, salarioNovo))    