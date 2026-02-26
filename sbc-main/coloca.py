peso = int(input("Coloque seu peso aqui: "))
altura = float(input("Coloque sua altura aqui: "))

IMC = peso / altura**2

print("Seu IMC é %.2f" %IMC)

if IMC< 18.5:
    print("Você está com baixo peso")
elif IMC>= 25:
    print("Você está pré-obeso")
elif IMC>= 30:
    print("Você está obeso grau I")
elif IMC>= 35:
    print("Você está obeso grau II")
elif IMC>= 40:
    print("Você está obeso grau III")
elif IMC>=18.6:
    print("Você está com o peso ideal")
