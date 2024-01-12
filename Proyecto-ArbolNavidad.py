# Arbol Navidad
def arbol_navidad(altura):
    # Hojas
    ancho = list( range(1, altura + 1) )
    for i in ancho:
        espacio = " " * (altura - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacio + asteriscos)
        
def main():
    # Solicitar al usuario la altura del árbol 
    altura_arbol = int(input("Ingrese la altura del árbol de Navidad: "))
    # Llamar a la función para imprimir el árbol
    arbol_navidad(altura_arbol)

if __name__ == "__main__":
    main()