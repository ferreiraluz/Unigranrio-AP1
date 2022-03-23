"""
4. Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
para o INSS e 5% para o sindicato, faça um programa que nos dê:
• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.
• calcule os descontos e o salário líquido, conforme a tabela abaixo:
o IR (11%) : R$
o INSS (8%) : R$
o Sindicato ( 5%) : R$
o Salário Líquido : R$
Obs: Salário Bruto - Descontos = Salário Líquido.
"""

salPorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadasNoMês = float(input("Quantas horas você trabalha no mês? "))

salarioBruto = salPorHora * horasTrabalhadasNoMês

 
percentualImpostoDeRenda =  salarioBruto*11/100
impostoDeRenda = salarioBruto - percentualImpostoDeRenda
print("Você pagará ao Imposto de Renda: R$ ", percentualImpostoDeRenda)

percentualINSS =  salarioBruto*8/100
impostoINSS = salarioBruto - percentualINSS
print("Você pagará ao INSS: R$ ", percentualINSS)

percentualSindicato =  salarioBruto*5/100
impostoSindicato = salarioBruto - percentualSindicato
print("Você pagará ao Sindicato: R$ ", percentualSindicato)

salarioLiquido = salarioBruto - percentualSindicato - percentualINSS - percentualImpostoDeRenda

print("Seu salário bruto: ", salarioBruto)
print("Seu salário líquido: ", salarioLiquido)

