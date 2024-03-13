#Faça um programa que calcule a area de um retângulo

LadoA: float
ladoB: float
area: float
resposta: str

ladoA = float(input('Digite o lado A: '))
ladoB = float(input('Digite o lado B: '))
area = ladoA * ladoB

#print(ladoA * ladoB) outra opção de printar a multiplicação de a vezes b. Colocando direto o print na area, estou nomeando a variavel.

resposta = 'A área do retângulo é' + str (area)

#print('A área do retângulo é ' , area)

###print(resposta)


#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu sálario no referido mês. 

hora: float
horasMes: float
totalHoras: float

hora = float(input('Digite quanto você ganha por hora: '))
horasMes = float(input('Digite quantas horas você trabalhou no mês: '))
totalHoras = hora * horasMes

print(totalHoras)

quantidadeDeHorasTrabalhadas: float
valorDaHora: float
total: float

quantidadeDeHorasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
valorDaHora = float(input('Digite o valor da hora: '))

total = quantidadeDeHorasTrabalhadas * valorDaHora

print('O total é:',total)



