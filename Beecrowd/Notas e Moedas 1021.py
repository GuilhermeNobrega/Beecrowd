x = float(input())
cem = (x//100)
x = x%100
cinquent = x//50
x = x%50
vinte = x//20
x = x%20
dez = x//10
x = x%10
cinco = x//5
x = x%5
dois = x//2
x = x%2

um_real = x//1.00
x = x%1
cqt_centavos = x//0.50
x = x%0.50
vntcinco_centavos = x//0.25
x = x%0.25
dz_centavos = x//0.10
x = x%0.10
cnc_centavos = x//0.05
x = x%0.05
um_centavo = x//0.01
x = x%0.01

print("NOTAS:")
print(f"{int(cem)} nota(s) de R$ 100.00")
print(f"{int(cinquent)} nota(s) de R$ 50.00")
print(f"{int(vinte)} nota(s) de R$ 20.00")
print(f"{int(dez)} nota(s) de R$ 10.00")
print(f"{int(cinco)} nota(s) de R$ 5.00")
print(f"{int(dois)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(um_real)} moedas(s) de R$ 1.00")
print(f"{int(cqt_centavos)} moedas(s) de R$ 0.50")
print(f"{int(vntcinco_centavos)} moedas(s) de R$ 0.25")
print(f"{int(dz_centavos)} moedas(s) de R$ 0.10")
print(f"{int(cnc_centavos)} moedas(s) de R$ 0.05")
print(f"{int(um_centavo)} moedas(s) de R$ 0.01")



