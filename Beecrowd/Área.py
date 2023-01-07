'''A = float(input())
B = float(input())
C = float(input())
pi = 3.14159
tri = A*C/2
cir = pi*C**2
tra = (A+B)*C/2
qua = B**2
ret = A*B
print(f"""TRIANGULO: {tri:.3f}
CIRCULO: {cir:.3f}
TRAPEZIO: {tra:.3f}
QUADRADO: {qua:.3f}
RETANGULO: {ret:.3f}""")'''
#Outra solução..
A,B,C = map(float, input().split())
pi = 3.14159
tri = A*C/2
cir = pi*C**2
tra = (A+B)*C/2
qua = B**2
ret = A*B
print(f"""TRIANGULO: {tri:.3f}
CIRCULO: {cir:.3f}
TRAPEZIO: {tra:.3f}
QUADRADO: {qua:.3f}
RETANGULO: {ret:.3f}""")

