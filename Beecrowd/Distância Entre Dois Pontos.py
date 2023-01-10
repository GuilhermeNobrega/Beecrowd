from math import pow
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
distancia =(x2-x1)**2 + (y2-y1)**2
raiz = pow(distancia,1/2)
print(f"{raiz:.4f}")

