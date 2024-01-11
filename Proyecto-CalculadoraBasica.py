# Suma de dos numeros
def suma(num1,num2):
    return num1 + num2

# Resta de dos numeros
def resta(num1,num2):
    return num1 - num2

# Multiplicacion de dos numeros
def multiplicacion(num1,num2):
    return num1 * num2

# Division de dos numeros
def division(num1,num2):
    if(num2 == 0):
        return "No se puede dividir entre 0"
    else:
        return num1 / num2

# Menu de opciones
def menu():
    while True:
        print("Selecciona la operacion: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        opcion = int( input("Digite su eleccion: ") )
        if(1 <= opcion <= 4):
            break
    return opcion

# Calculadora basica
def calculadoraBasica():
    print("Bienvenido a la calculadora basica")
    opcion = menu()
    num1 = int( input("Ingrese el primer numero: ") )
    num2 = int( input("Ingrese el segundo numero: ") )

    switch = {
        1: suma,
        2: resta,
        3: multiplicacion,
        4: division
    }
    
    '''Switch es un diccionario donde las claves son los números de las 
    operaciones (1, 2, 3, 4) y los valores son las funciones correspondientes 
    (suma, resta, multiplicacion, division).
    * switch[opcion] obtiene la ---función--- asociada a la opción seleccionada del diccionario. 
    Por ejemplo, si opcion es 1, obtendríamos la función suma. A este le pasamos los argumentos.
    * Si el usuario seleccionó la opción 1 (suma), resultado contendría '
    el resultado de llamar a suma(num1, num2).'''
    resultado = switch[opcion](num1, num2)
    print(resultado)
    
# Funcion principal
if __name__ == '__main__':
    calculadoraBasica()