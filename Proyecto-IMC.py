  
print("Calculadora IMC (Indice de Masa Corporal")
# Solicitamos al usuario su estatura y peso
estatura = float(input("Ingrese su estatura en centimetros (cm): ")) / 100 #convertimos a metros
peso = float(input("Ingrese su peso en kilogramos (Kg): "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar la estatura, peso y IMC por pantalla
print(f"Estatura: {estatura} metros")
print(f"Peso: {peso} kilogramos")
print(f"IMC: {round(imc,2)}")
    
# Clasificar el IMC en rangos y mostrar un mensaje correspondiente
if imc < 18.5:
    print("Clasificación: Bajo peso (delgado)")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso adecuado (aceptable)")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Clasificación: Obesidad grado 1")
elif 35 <= imc < 39.9:
    print("Clasificación: Obesidad grado 2")
else:
    print("Clasificación: Obesidad grado 3")