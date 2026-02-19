Ganha_Hora = int(input("Digite aqui o valor da sua hora "))
Hora_trabalhada = int(input("Digite aqui a quantidade de horas trabalhadas "))

bruto = Ganha_Hora * Hora_trabalhada
print("- Você ganha bruto %.2f" %bruto)

IR = bruto* 0.11
INSS = bruto* 0.08
SINDICATO = bruto* 0.05

print("- IR (11%%): R$ %.2f " %IR)
print("- INSS (8%%): R$ %.2f " %INSS)
print("- SINDICATO (5%%): R$ %.2f " %SINDICATO)

liquido = bruto - IR - INSS - SINDICATO
print('Você ganha R$ %.2f' %liquido)
