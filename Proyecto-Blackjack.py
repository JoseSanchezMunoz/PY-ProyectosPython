""" 
    El blackjack es un juego de cartas donde el objetivo es obtener una mano con un valor 
    lo más cercano posible a 21 sin pasarse. 
    - Las cartas numéricas cuentan por su valor. 
    - las cartas con figuras (J, Q, K) cuentan como 10
    - Los Ases pueden contar como 1 u 11.
    Si la suma de las cartas de un jugador supera 21, pierde automáticamente ("se pasa").

"""
    
def calcular_puntaje(mano):
    """
    Calcula la puntuación de una mano de blackjack: El mayor valor sin superar 21
    """
    puntaje = 0
    num_as = 0
    
    for carta in mano:
        if carta.isdigit(): # Si es un número
            puntaje += int(carta)
        elif carta in ['J', 'Q', 'K']: # Si es letra diferente de A, todos valen 10
            puntaje += 10
        elif carta == 'A':
            num_as += 1 # No aumentamos el puntaje con esto, solo contamos las As
    # Al final de este primer for tenemos el puntaje total sin contar las As, las cuales tendrán otro tratamiento

    # Contamos cada As como 1 para evitar superar 21 (si lo llega a superar con As 1 igual sería con 10. El jugador perdió desde el comienzo)
    for _ in range(num_as): # Iteramos el número de As encontradas (no necesita iterador ya que no lo usamos)
        puntaje += 1

    # Intentamos agregar 10 puntos por cada As, siempre que no nos pasemos de 21 (si ya lo habíamos pasado, ya se había perdido desde antes)
    for _ in range(num_as):
        if puntaje + 10 <= 21:
            puntaje += 10

    return puntaje

    
def blackjack_mayor_que(mano_1, mano_2):
    puntaje_mano1 = calcular_puntaje(mano_1)
    puntaje_mano2 = calcular_puntaje(mano_2)
    if (puntaje_mano1 <= 21 and puntaje_mano2 <= 21 and puntaje_mano1 > puntaje_mano2):
        return True
    elif (puntaje_mano1 <= 21 and puntaje_mano2 > 21):
        return True
    else:
        return False

# Indicacion: Solo se dice si el jugador 1 gana al 2, en caso de perder o empate se considera como que no gano

# Ejemplo donde el puntaje del jugador 1 y jugador 2 superaron los 21
mano_1 = ['J', 'Q', 'K']   # Puntaje total: 30
mano_2 = ['10', '9', 'K']       # Puntaje total: 29
print(f"Mano 1 gana a mano 2?  {blackjack_mayor_que(mano_1, mano_2)}")

# Ejemplo donde el puntaje del jugador 1 supera jugador 2 pero no 21
mano_3 = ['A', 'K', 'J']   # Puntaje total: 21
mano_4 = ['10', '9']       # Puntaje total: 19
print(f"Mano 3 gana a mano 4?  {blackjack_mayor_que(mano_3, mano_4)}")

# Ejemplo donde el puntaje del jugador 1 supera 21
mano_5 = ['Q', 'K', '6']   # Puntaje total: 26
mano_6 = ['10', '9']       # Puntaje total: 19
print(f"Mano 5 gana a mano 6?  {blackjack_mayor_que(mano_5, mano_6)}")

# Ejemplo donde el jugador 2 se pasa de 21
mano_7 = ['A', 'K', '10']  # Puntaje total: 21 (A cuenta como 1)
mano_8 = ['9', '7', '6']   # Puntaje total: 22
print(f"Mano 7 gana a mano 8?  {blackjack_mayor_que(mano_7, mano_8)}")

# Ejemplo de empate (ambos jugadores tienen el mismo puntaje)
mano_9 = ['J', '7']        # Puntaje total: 17
mano_10 = ['10', '7']      # Puntaje total: 17
print(f"Mano 9 gana a mano 10?  {blackjack_mayor_que(mano_9, mano_10)}")



