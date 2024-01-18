def esBisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio = int(input("Ingresa un año: "))
print(f"Es bisiesto? {esBisiesto(anio)}")
