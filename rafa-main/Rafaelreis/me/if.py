peso = int(input("Coloque seu peso aqui: "))
altura = float(input("Coloque sua altura aqui: "))

IMC = peso / altura**2

print("Seu IMC é %.2f" %IMC)

if IMC< 18.5:
    print("Você está com baixo peso")
if IMC<= 24.9:
    print("Você está com o peso ideal")
if IMC>= 25:
    print("Você está pré-obeso")
