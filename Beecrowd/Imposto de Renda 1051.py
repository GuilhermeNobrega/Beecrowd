x = float(input()) #duas casas decimais
if x>=0 and x<=2000:
    print('Isento')
elif x>=2000.1 and x <=3000:
    print("Teste 1")
    contas1 = (x-1000)
    contas2 = (1000*0.08)
    print(contas2)
    print(f"R$ {x:.2f}")
elif x>=3000.01 and x<=4500:
    contas3 = (x-1000)
    contas4 = (contas3*0.18)
    print(f"R$ {x:.2f}")
