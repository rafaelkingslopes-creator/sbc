A = int(input("Lado A: "))
B = int(input("Lado B: "))
C = int(input("Lado C: "))

if (A<B+C) and (B<A+C) and (C<A+B):
    if (A==B) and (B == C):
        print("Triangulo equilatero")
    else:
        if (A==B) or (A==C) or (B==C):
            print("Triangulo isósceles")
        else:
            print("Triangulo escaleno")
else:
    print("Não é um triangulo")