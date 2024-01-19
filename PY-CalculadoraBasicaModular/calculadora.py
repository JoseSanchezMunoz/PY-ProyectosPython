# Tengo 2 archivos: calculadora.py y operacionesCalculadora.py
# El alias de operacionesCalculadora (donde estan sumar, restar, multiplicar y dividir) será oc

# calculadora.py
import operacionesCalculadora as oc

numero1 = 10
numero2 = 2

reSuma = oc.suma(numero1, numero2)
reResta = oc.resta(numero1, numero2)
reMultiplicacion = oc.multiplicacion(numero1, numero2)
reDivision = oc.division(numero1, numero2)

# Mostrar resultados por consola
print(f"Suma: {reSuma}")
print(f"Resta: {reResta}")
print(f"Multiplicación: {reMultiplicacion}")
print(f"División: {reDivision}")



