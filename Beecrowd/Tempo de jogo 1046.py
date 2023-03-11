inicio,fim = map(int,input().split())
calculo = fim-inicio
if calculo<=0:
    calculo= calculo+24
print(f"O JOGO DUROU {calculo} HORA(S)")
