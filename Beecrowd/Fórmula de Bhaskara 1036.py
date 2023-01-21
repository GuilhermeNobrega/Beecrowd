a,b,c = map(float,input().split())
delta = b**2 - 4*a*c
if delta <0 or a==0:
    print("Impossivel calcular")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")