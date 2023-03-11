hora_inicial,minuto_inicial,hora_final,minuto_final = map(int,input().split())
calculo_horas = hora_final - hora_inicial
if calculo_horas <=0:
    calculo_horas = calculo_horas+24
elif calculo_horas ==1:
    calculo_horas = 0
calculo_minutos = minuto_final - minuto_inicial
if calculo_minutos <0:
    calculo_minutos = calculo_minutos+60
print(f"O JOGO DUROU {calculo_horas} HORA(S) E {calculo_minutos} MINUTO(S)")