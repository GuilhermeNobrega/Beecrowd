xdias = int(input())

ano = xdias//365 #ano
xdias = xdias%365 #dias

mes = xdias//30
xdias = xdias%30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{xdias} dia(s)")
