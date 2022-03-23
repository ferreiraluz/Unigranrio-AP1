     
'''
     Tendo como dado de entrada a altura (h) de uma pessoa, construa um
    algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    • Para home1.ns: (72.7*h) - 58
    • Para mulheres: (62.1*h) - 44.7
'''
   
h = float(input("Digite sua altura: "))
sexo = input("Você é homem ou mulher? ")

pesoIdealHomens = (72.7*h) - 58
pesoIdealMulheres = (62.1*h) - 44.7

if(sexo == "homem"):
    print("Seu peso ideal é", pesoIdealHomens)
elif(sexo == "mulher"):
    print("Seu peso ideal é", pesoIdealMulheres)



