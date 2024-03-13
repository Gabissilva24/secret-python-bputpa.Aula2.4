inteiros: int
inteiros2: int
reais: float

#produto=resultado da multiplicação

inteiros = int(input('Digite um número inteiro: '))
inteiros2 = int(input('Digite um número inteiro: '))
reais = float(input('Digite um número real: '))



calculo1:float
calculo2: float
calculo3: float
calculo4: float

calculo1 = (inteiros * 2) + (inteiros2 / 2) #para pegar mentade de um nuero basta dividir por dois ou multiplicar por 0.5
print(calculo1)
calculo2 = (inteiros * 3) + (reais)
print(calculo2)
calculo3 = reais ** 3 #elevar(potencia) em python colocar dois **
print(calculo3)
calculo4 = inteiros2 ** (1/3) #raiz cúbica
print(calculo4)


print(calculo1)
print(calculo2)
print(calculo3)
print(calculo4)
