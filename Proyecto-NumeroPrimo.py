def esPrimo(numero):
    if numero <= 1: # 1 o 0 no son primos
        return False
    elif numero == 2:
        return True # El 2 es primo
    elif numero % 2 == 0:
        return False # Los pares no son primos
    else: 
        for i in range(3, numero, 2):
            if numero % i == 0:
                return False
        # Si tras el recorrido por todo numero menos el que ingresamos
        # no se halla otro divisor exacto, es porque es primo
        return True 

num = int(input("Ingresa un numero: "))
print(f"Es primo? {esPrimo(num)}")