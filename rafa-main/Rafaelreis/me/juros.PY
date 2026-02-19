C = float(input("Quanto é o capital inicial: "))
I = float(input("Quanto é a taxa de juros: "))
T = int(input("Quantos periodos sao: "))

M = C * ( 1 + I)**T

print("O montante final é %2f" %M)
      
