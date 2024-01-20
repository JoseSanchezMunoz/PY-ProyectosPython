def buscar_palabra(doc_list, palabra_clave):
    """
    Toma una lista de documentos y una palabra clave.
    Devuelve una lista de índices en la lista original para todos los documentos que contienen la palabra clave.
    
    Argumentos:
    - doc_list (List[str]): Lista de documentos, donde cada documento es una cadena.
    - palabra_clave (str): Palabra clave a buscar en los documentos.
    
    Salida:
    - List[int]: Lista de índices en la lista original para los documentos que contienen la palabra clave.
    """
    # Inicializa una lista para almacenar los índices de los documentos que contienen la palabra clave
    indices = []
    # Convierte la palabra clave a minúsculas para hacer la búsqueda insensible a mayúsculas y minúsculas
    palabra_clave_minuscula = palabra_clave.lower()
    # Itera sobre la lista de documentos con sus índices
    for i, doc in enumerate(doc_list):
        # Elimina puntos y comas, y convierte a minúsculas para comparación
        doc_limpiado = doc.replace('.', '').replace(',', '').lower()  
        # Verifica si la palabra clave está presente como una palabra completa en el documento
        if palabra_clave_minuscula in doc_limpiado.split():
            # Si es así, agrega el índice del documento a la lista de índices
            indices.append(i)
    # Devuelve la lista de índices de documentos que contienen la palabra clave
    return indices


def busqueda_multiple(doc_list, palabras_clave):
    """
    Toma una lista de documentos y una lista de palabras clave.
    Devuelve un diccionario donde cada clave es una palabra clave y el valor es una lista de índices de documentos
    que contienen esa palabra clave.
    
    Argumentos:
    - doc_list (List[str]): Lista de documentos, donde cada documento es una cadena.
    - palabras_clave (List[str]): Lista de palabras clave a buscar en los documentos.
    
    Salida:
    - Dict[str, List[int]]: Diccionario donde las claves son palabras clave y los valores son listas de índices
      de documentos que contienen cada palabra clave.
    """
    # Inicializa un diccionario para almacenar los índices de documentos para cada palabra clave
    indices_palabras_clave = {}
    # Itera sobre la lista de palabras clave
    for palabra_clave in palabras_clave:
        # Convierte la palabra clave a minúsculas para hacer la búsqueda insensible a mayúsculas y minúsculas
        palabra_clave_minuscula = palabra_clave.lower()
        # Inicializa una lista para almacenar los índices de documentos que contienen la palabra clave actual
        indices_palabras_clave[palabra_clave_minuscula] = []
        # Itera sobre la lista de documentos con sus índices
        for i, doc in enumerate(doc_list):
            # Elimina puntos y comas, y convierte a minúsculas para comparación
            doc_limpiado = doc.replace('.', '').replace(',', '').lower()
            # Verifica si la palabra clave está presente como una palabra completa en el documento
            if palabra_clave_minuscula in doc_limpiado.split():
                # Si es así, agrega el índice del documento a la lista de índices para la palabra clave actual
                indices_palabras_clave[palabra_clave_minuscula].append(i)
    # Devuelve el diccionario con los índices de documentos para cada palabra clave
    return indices_palabras_clave


# Lo que nos devuelve es el indice donde se encuentra la palabra, es decir, el libro cuyo titulo
# coincide con la palabra clave

# Inicializamos una lista de prueba
doc_list = ["El descubrimiento de los rayos X revolucionó la medicina.", 
            "La teoría de la relatividad de Einstein cambió nuestra comprensión del espacio y el tiempo.", 
            "El método científico es fundamental para la investigación en todas las disciplinas."]

# Ejemplo de uso de buscar_palabra individual
palabra_individual = 'método'
resultado_individual = buscar_palabra(doc_list, palabra_individual)
print(f"\nTitulos de documentos relacionados\nResultado de buscar_palabra (indices): {resultado_individual}")

# Ejemplo de uso de busqueda_multiple
palabras_multiples = ['medicina', 'teoría', 'el']
resultado_multiples = busqueda_multiple(doc_list, palabras_multiples)
print(f"\nTitulos de documentos relacionados\nResultado de busqueda_multiple: {resultado_multiples}")

