x = int(input()) #Valor em segundos
horas_segundos = x//3600 # horas
x = x%3600
minutos_segundos = x//60 #minutos
resto_segundos = x%60 #segundos
print(f"{horas_segundos}:{minutos_segundos}:{resto_segundos}")