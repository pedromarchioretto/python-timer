import time
import re

tempo = input("quantos segundos você quer? ").replace(" ", "")
tempo = int(re.sub(r"[^0-9]", "", tempo))


horas = tempo // 3600
segundos = tempo % 3600
minutos = segundos // 60
segundos %= 60


for x in range (0, tempo + 1):
    if segundos < 10:
        secs_visor = "0" + str(segundos)
    else:
        secs_visor = segundos

    if minutos < 10:
        mins_visor = "0" + str(minutos)
    else:
        mins_visor = minutos

    if horas < 10:
        hrs_visor = "0" + str(horas)
    else:
        hrs_visor = horas


    print (f"{hrs_visor}:{mins_visor}:{secs_visor}") 

    if (horas != 0 and minutos != 0 and segundos != 0) or (horas == 0 and minutos == 0 and segundos != 0):
        segundos -= 1
    elif horas != 0 and minutos != 0 and segundos == 0:
        minutos -= 1
        segundos = 59
    elif horas != 0 and minutos == 0 and segundos == 0:
        horas -= 1
        minutos = 59
        segundos = 59
    elif horas == 0 and minutos != 0 and segundos == 0:
        minutos -= 1
        segundos = 59
    elif horas == 0 and minutos != 0 and segundos != 0:
        segundos -= 1
    elif horas != 0 and minutos == 0 and segundos != 0:
        segundos -= 1
    elif horas == 0 and minutos == 0 and segundos == 0:
        print("O TEMPO ACABOU!")

    time.sleep(1)

    