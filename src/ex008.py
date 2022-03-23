'''
    8. Faça um programa que leia um número indeterminado de valores,
    correspondentes a notas, encerrando a entrada de dados quando for informado
    um valor igual a -1 (que não deve ser armazenado). Após esta entrada de
    dados, faça: 
    o Mostre a quantidade de valores que foram lidos;
    o Exiba todos os valores na ordem em que foram informados, um ao lado
    do outro;
    o Exiba todos os valores na ordem inversa à que foram informados, um
    abaixo do outro;
    o Calcule e mostre a soma dos valores;
    o Calcule e mostre a média dos valores;
    o Calcule e mostre a quantidade de valores acima da média calculada;
    o Calcule e mostre a quantidade de valores abaixo de sete;
    o Encerre o programa com uma mensagem;
'''


numeros = 0 # recebe os valores fora do array, para permitir a utilização de métodos matemáticos
notas = [] # array que recebe os números
soma = 0
media = 0 # a lógica da média é a soma dividido pela quantidade de provas que o aluno fez.
contador = 0 
numeros = int(input("Digite a sua nota: [ Digite -1 para finalizar o programa ] "))


while numeros != -1:
    
    contador = contador + 1
    notas.append(numeros) # guardando os numeros colocados num array de notas

    
    
   

    soma += numeros
    media = soma / contador
    notasMaioresQueaMedia = list(filter(lambda n: n > media, notas)) # filtra as notas maiores que a média no array
    quantidadeNotasMaioresQueaMedia = len(notasMaioresQueaMedia) # mostra a quantidade de notas
    notasMenoresQueSete = list(filter(lambda n: n < 7, notas)) # filtra notas menores que 7
    quantidadeNotasMenoresQueSete = len(notasMenoresQueSete)

    numeros = int(input("Digite a sua nota: [ Digite -1 para finalizar o programa ] "))
    



print("A quantidade de notas armazenadas foi {}".format(contador))
print("Suas notas foram {}".format(notas)) 
notas.reverse()
print("Suas notas em ordem inversa são {}".format(notas)) 
print("Suas notas somadas são: {}".format(soma))
print("A média das suas notas é: {}".format(media))
print("Você tirou {} notas maiores que sua média. As suas notas maiores que a média são {}".format(quantidadeNotasMaioresQueaMedia,notasMaioresQueaMedia))
print("Você tirou {} notas menores que 7. As suas notas menores que 7 são {}".format(quantidadeNotasMenoresQueSete,notasMenoresQueSete))

print("Obrigado por usar o programa! : )") # finalizando com uma mensagem
