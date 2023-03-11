A,B,C = map(float,input().split())
lista = [A,B,C]
lista.sort(reverse=True)
A,B,C = lista
#print(A,B,C)
if A>=B+C:
    print("NAO FORMA TRIANGULO")
elif (A**2)==(B**2)+(C**2):
    print("TRIANGULO RETANGULO")
elif (A**2)>(B**2)+(C**2):
    print("TRIANGULO OBTUSANGULO")
elif (A**2)<(B**2)+(C**2):
    print("TRIANGULO ACUTANGULO")
if (A==B==C):
    print("TRIANGULO EQUILATERO")
elif (C==B or B==A):
    print("TRIANGULO ISOSCELES")