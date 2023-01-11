x = int(input())

cem = (x//100)
x = x%100
print(f"{cem} nota(s) de R$ 100,00")
cinquent = x//50
x = x%50
print(f"{cinquent} nota(s) de R$ 50,00")
vinte = x//20
x = x%20
print(f"{vinte} nota(s) de R$ 20,00")
dez = x//10
x = x%10
print(f"{dez} nota(s) de R$ 10,00")
cinco = x//5
x = x%5
print(f"{cinco} nota(s) de R$ 5,00")
dois = x//2
x = x%2
print(f"{dois} nota(s) de R$ 2,00")
um = x//1
x = x%1
print(f"{um} nota(s) de R$ 1,00")
#Jeito correto..
x = int(input())
print(x)
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
um = x//1
x = x%1
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquent} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")







