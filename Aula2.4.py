ganhoPorHora: float
horasTrabalhadasNoMes: float
salarioBruto: float
pagoINSS: float
pagoSindicato: float
pagoIR: float
salarioLiquido: float
totalDeDesconto: float




ganhoPorHora = float(input('Digite quanto você ganha por hora: '))
horasTrabalhadasNoMes = float(input('Digite quantas horas trabalhou no mês: '))
salarioBruto = (ganhoPorHora * horasTrabalhadasNoMes)
print(salarioBruto)
pagoINSS = (salarioBruto * 8) / 100
print(pagoINSS)
pagoIR = (salarioBruto * 11) / 100
print(pagoIR)
pagoSindicato = (salarioBruto * 5) / 100
print(pagoSindicato)
totalDeDesconto = (salarioBruto * 24) / 100
print(totalDeDesconto)
salarioLiquido = (salarioBruto - totalDeDesconto)
print(salarioLiquido)


