'''x =float(input(""))
if x <=400:
    print(f"Novo salario: {x+(x*0.15):.2f}")
    print(f"Reajuste ganho: {x*0.15}")
    print("Em percentual: 15 %")
elif x <=800:
    print(f"Novo salario: {x + (x * 0.12):.2f}")
    print(f"Reajuste ganho: {x * 0.12:.2f}")
    print("Em percentual: 12 %")
elif x <=1200.00:
    print(f"Novo salario: {x + (x * 0.10):.2f}")
    print(f"Reajuste ganho: {x * 0.10:.2f}")
    print("Em percentual: 10 %")
elif x <=2000.00:
    print(f"Novo salario: {x + (x * 0.07):.2f}")
    print(f"Reajuste ganho: {x * 0.07:.2f}")
    print("Em percentual: 7 %")

else:
    print(f"Novo salario: {x + (x * 0.04):.2f}")
    print(f"Reajuste ganho: {x * 0.04:.2f}")
    print("Em percentual: 7 %")'''


x = float(input())
if x >=0 and x <=400:
    conta = x*0.15
    conta1 = x+conta
    perc = 15
elif x >=400.01 and x <=800:
    conta = x*0.12
    conta1 = x+conta
    perc = 12
elif x >=800.01 and x <=1200:
    conta = x*0.10
    conta1 = x+conta
    perc = 10
elif x >= 1200.01 and x <=2000:
    conta = x*0.07
    conta1 = x+conta
    perc = 7
else:
    conta = x*0.04
    conta1 = x+conta
    perc = 4
print(f"Novo salario: {conta1:.2f}")
print(f"Reajuste: {conta:.2f}")
print(f"Percentual: {perc} %")
