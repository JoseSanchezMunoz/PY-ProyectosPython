import random as rd

# Menu de opciones
def menu():
    while True:
        print("Selecciona la operacion: ")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        try:
            opcion = int(input("Digite su elección: "))
            if 1 <= opcion <= 3:
                break
            else:
                print("Ingrese un número entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido")
            
    return opcion

# Que signo representa el numero elegido
def manoEs(op):
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
    return opciones[op]

# Que elige el bot
def eleccionBot():
    bot = manoEs(rd.randint(1, 3))
    return bot

# Que elige el jugador
def eleccionJugador(op):
    jugador = manoEs(op)
    bot = eleccionBot()

    combinaciones_ganadoras = [("Piedra", "Tijeras"), ("Papel", "Piedra"), ("Tijeras", "Papel")]

    if jugador == bot:
        print(f"Jugador: {jugador} (Empate) Vs Bot: {bot} (Empate)")
    elif (jugador, bot) in combinaciones_ganadoras:
        print(f"Jugador: {jugador} (Gana) Vs Bot: {bot} (Pierde)")
    else:
        print(f"Jugador: {jugador} (Pierde) Vs Bot: {bot} (Gana)")
    
# Juego
def piedraPapelTijeras():
    print("Bienvenido al juego de Piedra, Papel o Tijeras")
    opcion = menu()
    eleccionJugador(opcion)
    
# Funcion principal
if __name__ == '__main__':
    piedraPapelTijeras()
    