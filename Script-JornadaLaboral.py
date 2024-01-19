# La horas y minutos se modifican con hour y minute

from datetime import datetime

# Obtenemos la hora actual
horaActual = datetime.now()
# Imprimimos la hora actual
print(f"Hora actual: {horaActual.strftime('%H:%M:%S')}")

# Definimos la hora de finalización de la jornada laboral
horaSalida = horaActual.replace(hour=18, minute=30, second=0)
print(f"Hora de Salida: {horaSalida.strftime('%H:%M:%S')}")

# Verificamos si es hora de finalizar la jornada laboral
if horaActual >= horaSalida:
    print("Terminó la jornada laboral")
else:
    # Calculamos el tiempo restante
    tiempoRestante = horaSalida - horaActual
    horas, segundos = divmod(tiempoRestante.seconds, 3600)
    minutos, segundos = divmod(segundos, 60)
    # Imprimimos el tiempo restante
    print(f"Tiempo restante: {horas} horas, {minutos} minutos y {segundos} segundos.")