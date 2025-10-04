import csv
import statistics
from operator import itemgetter # Se utiliza para el ordenamiento eficiente de diccionarios

# --- CONSTANTES ---
# Simulación de la estructura de datos que sería leída de un archivo CSV.
# En un entorno real, esta lista se llenaría mediante la función 'cargar_datos_csv'.
DATOS_CSV_MOCK = [
    {'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'},
    {'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'},
    {'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'},
    {'nombre': 'Alemania', 'poblacion': 83149300, 'superficie': 357022, 'continente': 'Europa'},
    {'nombre': 'Canadá', 'poblacion': 38246108, 'superficie': 9984670, 'continente': 'América'},
    {'nombre': 'China', 'poblacion': 1411778724, 'superficie': 9596960, 'continente': 'Asia'},
    {'nombre': 'Australia', 'poblacion': 25700000, 'superficie': 7692024, 'continente': 'Oceanía'},
]

# --- MODULARIZACIÓN Y FUNCIONES PRINCIPALES ---

def cargar_datos_csv(ruta_archivo: str = None) -> list:
    """
    Simula la carga de datos desde un archivo CSV y los convierte
    a una lista de diccionarios, como se requiere en el TPI.
    
    Controla errores de formato al convertir Población y Superficie a 'int'.
    """
    print(f"Simulando carga de datos desde CSV (usando mock data)...")
    datos_estructurados = []
    
    # Usamos la lista de mock data como si fuera la data leída
    for registro in DATOS_CSV_MOCK:
        try:
            # Conversión de tipos obligatoria (Población y Superficie deben ser 'int')
            # Las variables ingresadas por input() o leídas de un archivo (simuladas aquí)
            # deben convertirse si se necesitan como números para cálculos [17, 18].
            pais = {
                'nombre': registro['nombre'],
                'poblacion': int(registro['poblacion']),
                'superficie': int(registro['superficie']),
                'continente': registro['continente']
            }
            datos_estructurados.append(pais)
        except ValueError:
            # Manejo de error de formato en el CSV [18].
            print(f"⚠️ Error de formato en el registro: {registro['nombre']}. Omitiendo.")
            continue
            
    print(f"✅ Datos cargados correctamente. Total de países: {len(datos_estructurados)}")
    return datos_estructurados

def mostrar_pais(pais: dict):
    """Muestra la información de un país usando f-strings [19]."""
    print("--- País ---")
    print(f"Nombre: {pais['nombre']}")
    # Uso de formato para números grandes (no requerido, pero mejora la legibilidad)
    print(f"Población: {pais['poblacion']:,} habs.")
    print(f"Superficie: {pais['superficie']:,} km²")
    print(f"Continente: {pais['continente']}")
    print("-" * 15)

def buscar_pais_por_nombre(datos: list):
    """
    Busca países por coincidencia parcial o exacta de nombre.
    Usa el operador 'in' para la coincidencia parcial [20].
    """
    busqueda = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    resultados = []
    
    if not busqueda:
        print("Búsqueda inválida. Intente de nuevo.")
        return

    for pais in datos:
        if busqueda in pais['nombre'].lower():
            resultados.append(pais)
    
    if resultados:
        print(f"\n--- Resultados de búsqueda para '{busqueda}' ({len(resultados)} encontrados) ---")
        for pais in resultados:
            mostrar_pais(pais)
    else:
        # Manejo de búsqueda sin resultados [18].
        print(f"\n❌ No se encontraron países que coincidan con '{busqueda}'.")

def filtrar_por_continente(datos: list):
    """Filtra países por continente usando listas y el operador 'in' [20]."""
    continente_buscado = input("Ingrese el continente a filtrar (América, Asia, Europa, Oceanía): ").strip().title()
    
    # Crear una lista de continentes válidos para la validación de entrada
    continentes_validos = ["América", "Asia", "Europa", "Oceanía"]
    
    # Validar que el continente ingresado sea uno de los válidos (lógica condicional)
    if continente_buscado not in continentes_validos:
        print(f"❌ Continente inválido: {continente_buscado}. Por favor, ingrese uno válido.")
        return

    resultados = []
    for pais in datos:
        if pais['continente'] == continente_buscado: # Condicional simple [21]
            resultados.append(pais)

    if resultados:
        print(f"\n--- Países en {continente_buscado} ({len(resultados)} encontrados) ---")
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print(f"\n❌ No se encontraron países en {continente_buscado}.")

def filtrar_por_rango(datos: list, clave: str, unidad: str):
    """
    Filtra países por rango de Población o Superficie.
    Implementa anidamiento de validación y lógica compleja (if/elif/else anidado o encadenado) [22, 23].
    """
    print(f"\n--- Filtro por Rango de {clave.title()} ({unidad}) ---")
    try:
        min_val = float(input(f"Ingrese el valor mínimo de {clave}: "))
        max_val = float(input(f"Ingrese el valor máximo de {clave}: "))
    except ValueError:
        print("❌ Valores ingresados inválidos. Debe ser un número.")
        return

    # Aseguramos que el mínimo sea menor o igual al máximo (validación)
    if min_val > max_val:
        min_val, max_val = max_val, min_val
        print(f"Ajustando rango: Mínimo {min_val}, Máximo {max_val}")
        
    resultados = []
    
    for pais in datos:
        valor = pais[clave]
        # Lógica de rango usando encadenamiento de comparaciones y operador 'and' [24, 25].
        if min_val <= valor <= max_val:
            resultados.append(pais)

    if resultados:
        print(f"\n--- Países con {clave} entre {min_val:,} y {max_val:,} {unidad} ---")
        for pais in resultados:
            mostrar_pais(pais)
    else:
        print("❌ No se encontraron países en ese rango.")

def ordenar_paises(datos: list):
    """Ordena la lista de países por clave y dirección (ascendente/descendente)."""
    
    # Uso de listas para definir las opciones permitidas
    claves_validas = {'1': 'nombre', '2': 'poblacion', '3': 'superficie'}
    ordenes_validos = {'1': False, '2': True} # False = Ascendente, True = Descendente [26]
    
    print("\nOpciones de Ordenamiento:")
    print(" 1. Nombre (Alfabético)")
    print(" 2. Población (Numérico)")
    print(" 3. Superficie (Numérico)")
    
    opcion_clave = input("Elija clave para ordenar (1-3): ")
    if opcion_clave not in claves_validas:
        print("❌ Opción de clave inválida.")
        return

    clave_seleccionada = claves_validas[opcion_clave]

    print("\nDirección de Ordenamiento:")
    print(" 1. Ascendente (A-Z, 0-9)")
    print(" 2. Descendente (Z-A, 9-0)")
    
    opcion_orden = input("Elija dirección (1-2): ")
    if opcion_orden not in ordenes_validos:
        print("❌ Opción de ordenamiento inválida.")
        return
        
    orden_descendente = ordenes_validos[opcion_orden]

    # Usamos sorted() para generar una nueva lista ordenada. 
    # Usamos itemgetter del módulo operator para usar la clave del diccionario como criterio de ordenamiento.
    # itemgetter es un recurso avanzado de la librería estándar, permitido si la lógica lo requiere.
    datos_ordenados = sorted(datos, key=itemgetter(clave_seleccionada), reverse=orden_descendente)

    print(f"\n--- Países Ordenados por {clave_seleccionada.title()} ---")
    for pais in datos_ordenados:
        mostrar_pais(pais)

def calcular_min_max(datos: list, clave: str, tipo: str) -> dict:
    """Calcula y muestra el país con mayor o menor valor para una clave específica."""
    if not datos:
        return {"resultado": "Lista vacía"}

    # Utilizamos la función max/min con el argumento key para encontrar el país [26]
    if tipo == 'mayor':
        pais_encontrado = max(datos, key=itemgetter(clave))
    else: # tipo == 'menor'
        pais_encontrado = min(datos, key=itemgetter(clave))

    print(f"\n--- País con {tipo.title()} {clave.title()} ---")
    mostrar_pais(pais_encontrado)
    return pais_encontrado

def calcular_promedio(datos: list, clave: str):
    """Calcula y muestra el promedio de una clave numérica."""
    if not datos:
        print(f"\n❌ No hay datos para calcular el promedio de {clave}.")
        return 0

    # Extraer los valores en una lista temporal
    valores = [pais[clave] for pais in datos] # Comprensión de listas [27, 28]
    
    # Usamos la función mean del módulo statistics, que fue requerido en el Ejercicio 6 del TP3 [13, 29].
    # También se puede implementar manualmente usando sum() y len() [13, 30, 31].
    try:
        promedio = statistics.mean(valores)
        print(f"El promedio de {clave} es: {promedio:,.2f}")
        return promedio
    except statistics.StatisticsError:
        print(f"❌ No se pudo calcular el promedio de {clave} (posiblemente datos no numéricos).")
        return 0

def contar_por_continente(datos: list):
    """Calcula y muestra la cantidad de países por continente."""
    
    # Uso de diccionarios para agrupar y contar [8]
    conteo = {} # Se crea un diccionario vacío {} [32]
    for pais in datos:
        continente = pais['continente']
        # Lógica condicional: si el continente ya existe en el diccionario, incrementa, si no, lo inicializa
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1

    print("\n--- Cantidad de Países por Continente ---")
    # Itera sobre las claves y valores del diccionario (método items()) [33].
    for continente, cantidad in conteo.items():
        print(f"{continente}: {cantidad} países")

def ejecutar_estadisticas(datos: list):
    """
    Coordina y presenta todas las estadísticas requeridas.
    (Modularidad: esta función llama a sub-funciones para cada cálculo) [34].
    """
    print("\n========== ESTADÍSTICAS GLOBALES ==========")
    
    # Min/Max Población
    calcular_min_max(datos, 'poblacion', 'mayor')
    calcular_min_max(datos, 'poblacion', 'menor')

    # Promedios
    calcular_promedio(datos, 'poblacion')
    calcular_promedio(datos, 'superficie')

    # Cantidad por Continente
    contar_por_continente(datos)
    
    print("==========================================")


# --- FUNCIÓN PRINCIPAL Y MENÚ DE NAVEGACIÓN ---

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n===== MENÚ DE GESTIÓN DE PAÍSES =====")
    print("1. Buscar país por nombre")
    print("2. Filtrar por Continente")
    print("3. Filtrar por Rango de Población")
    print("4. Filtrar por Rango de Superficie")
    print("5. Ordenar países")
    print("6. Mostrar Estadísticas")
    print("7. Salir")
    print("======================================")

def main():
    """Función principal del programa. Ejecuta el bucle del menú."""
    
    # 1. Carga inicial de datos
    datos_paises = cargar_datos_csv()
    
    # 2. Bucle principal (estructura repetitiva 'while') [35]
    while True:
        mostrar_menu()
        
        # Pedimos el input del usuario y lo convertimos a entero si es posible
        opcion_str = input("Seleccione una opción (1-7): ").strip()
        
        # Validación de entrada (manejo de error básico para números) [18]
        try:
            opcion = int(opcion_str)
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número del 1 al 7.")
            continue # Continúa con la siguiente iteración del bucle [36, 37]

        # 3. Lógica condicional (if-elif-else) [23]
        if opcion == 1:
            buscar_pais_por_nombre(datos_paises)
        elif opcion == 2:
            filtrar_por_continente(datos_paises)
        elif opcion == 3:
            # Uso de funciones para delegar la complejidad
            filtrar_por_rango(datos_paises, 'poblacion', 'habs.')
        elif opcion == 4:
            filtrar_por_rango(datos_paises, 'superficie', 'km²')
        elif opcion == 5:
            ordenar_paises(datos_paises)
        elif opcion == 6:
            ejecutar_estadisticas(datos_paises)
        elif opcion == 7:
            print("Saliendo del sistema. ¡Adiós!")
            break # Detiene el bucle inmediatamente [38, 39]
        else:
            print("❌ Opción no reconocida. Por favor, intente con 1-7.")

# Ejecución del programa (punto de inicio)
if __name__ == "__main__":
    main()
