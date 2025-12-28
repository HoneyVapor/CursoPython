"""
ARCHIVO: main.py
OBJETIVO: Ruta de aprendizaje para programadores de C.
SINTAXIS: Python 3.x
"""

"""
ARCHIVO: main.py (Guía Maestra para Programadores de C)
Este script funciona como un tutorial ejecutable. 
Cada función detalla un choque cultural entre C y Python.
"""

# =============================================================================
# 0. LA IDENTACIÓN: EL REEMPLAZO DE LAS LLAVES { }
# =============================================================================
def leccion_0_indentacion():
    print("--- LECCIÓN 0: IDENTACIÓN (SINTAXIS VISUAL) ---")
    
    # En C: Las llaves { } definen el alcance (scope). El espacio en blanco es ignorado.
    # En Python: NO hay llaves. El espacio en blanco al inicio es OBLIGATORIO.
    
    valor = 10
    if valor > 5:
        # Todo lo que esté indentado (normalmente 4 espacios) pertenece al IF.
        print("  Este print está dentro del IF porque tiene espacios a la izquierda.")
        if valor == 10:
            print("    Este tiene doble indentación, está dentro del segundo IF.")
    
    print("Este print está fuera del IF porque volvió al margen izquierdo.")
    
    # ERROR COMÚN: Mezclar tabuladores y espacios causará un IndentationError.
    # Python usa el espaciado para saber dónde termina una función o un bucle.
    print("-" * 30)

# =============================================================================
# 1. GESTIÓN DE MEMORIA Y TIPADO
# =============================================================================
def leccion_1_memoria():
    print("--- LECCIÓN 1: MEMORIA Y OBJETOS ---")
    
    # En C: int a = 5; 
    # El compilador reserva 4 bytes en una dirección fija (ej. 0x7ffd).
    # Si haces a = "hola", el compilador de C explota.
    
    # En Python: Todo es una REFERENCIA a un objeto.
    a = 5  
    # 'a' no es una caja, es una etiqueta apuntando a un objeto de tipo int que vale 5.
    print(f"1. Valor de a: {a} (ID/Dirección: {id(a)})")
    
    a = "Hola mundo" 
    # Ahora la etiqueta 'a' apunta a un objeto string. 
    # El objeto '5' anterior queda huérfano y el Garbage Collector lo borrará.
    print(f"2. a cambió a string sin errores: {a} (Nueva ID: {id(a)})")
    print("-" * 30)

# 

# =============================================================================
# 2. ESTRUCTURAS DE DATOS (ADIÓS A LOS PUNTEROS)
# =============================================================================
def leccion_2_estructuras():
    print("--- LECCIÓN 2: ESTRUCTURAS DINÁMICAS ---")
    
    # En C: Para una lista dinámica necesitas malloc(), realloc() y free().
    # En Python: La clase 'list' es un array dinámico que gestiona su tamaño.
    mi_lista = [10, 20, 30]
    mi_lista.append(40) # Automáticamente redimensiona el heap.
    
    # Diccionarios (Equivalente a una Hash Map compleja en C)
    # No tienes que implementar la función hash; ya viene optimizada.
    edades = {"Alice": 25, "Bob": 30}
    
    print(f"Lista (Array dinámico): {mi_lista}")
    print(f"Diccionario (Hash Map): {edades['Alice']}")
    
    # Tuplas: Son como listas pero INMUTABLES (no puedes cambiar sus valores).
    # Útiles para asegurar que los datos no se corrompan accidentalmente.
    punto_fijo = (10, 20) 
    print(f"Tupla (Inmutable): {punto_fijo}")
    print("-" * 30)


# =============================================================================
# 3. CONTROL DE FLUJO Y EL "PYTHONIC WAY"
# =============================================================================
def leccion_3_iteracion():
    print("--- LECCIÓN 3: BUCLES E ITERADORES ---")
    
    items = ["CPU", "RAM", "GPU"]
    
    # ESTILO C (Iterar por índice):
    # Aunque funciona, en Python se considera "poco elegante".
    print("Iteración estilo C:")
    for i in range(len(items)):
        print(f"  Índice {i}: {items[i]}")
        
    # ESTILO PYTHON (Iteración directa):
    # Python usa el protocolo de 'Iteradores'. Accedes al objeto directamente.
    print("\nIteración estilo Python:")
    for componente in items:
        print(f"  Componente: {componente}")
        
    # LIST COMPREHENSIONS:
    # Una forma de crear listas en una sola línea (Sintaxis Matemática).
    # En C requeriría un bucle for y múltiples líneas de código.
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [n**2 for n in numeros if n > 2]
    print(f"\nCuadrados de n > 2: {cuadrados}")
    print("-" * 30)

# 

# =============================================================================
# 4. MANEJO DE ERRORES (EXCEPCIONES VS RETURN CODES)
# =============================================================================
def leccion_4_excepciones():
    print("--- LECCIÓN 4: GESTIÓN DE ERRORES ---")
    
    # En C: Las funciones suelen devolver -1 o NULL si fallan.
    # En Python: Usamos Try/Except (Excepciones).
    
    divisor = 0
    try:
        # Intentamos una operación peligrosa
        resultado = 10 / divisor
    except ZeroDivisionError:
        # Capturamos el error específico sin que el programa muera
        print("Error: Intentaste dividir por cero, pero lo controlamos.")
    finally:
        # Esto se ejecuta siempre (útil para cerrar archivos, como un fclose)
        print("Limpieza de recursos finalizada.")
    print("-" * 30)

# =============================================================================
# 5. CLASES Y OBJETOS (STRUCTS CON COMPORTAMIENTO)
# =============================================================================
def leccion_5_poo():
    print("--- LECCIÓN 5: CLASES (POO) ---")
    
    # En C: Usas 'struct' para agrupar datos.
    # En Python: Una 'class' agrupa datos Y las funciones que actúan sobre ellos.
    
    class PunteroVirtual:
        def __init__(self, x, y):
            self.x = x # 'self' es equivalente al puntero 'this' o al objeto actual.
            self.y = y
            
        def mostrar(self):
            print(f"Coordenadas: ({self.x}, {self.y})")

    p = PunteroVirtual(10, 20)
    p.mostrar()
    print("-" * 30)

# =============================================================================
# 6. PUNTO DE ENTRADA (EL EQUIVALENTE A main())
# =============================================================================
if __name__ == "__main__":
    # Esta condición es crucial. 
    # En C, el cargador busca la función 'main'. 
    # En Python, el intérprete lee el archivo de arriba abajo.
    # Esta línea asegura que el código solo se ejecute si corres el archivo directamente,
    # no si lo importas desde otro script.
    
    print("EJECUTANDO RUTA DE APRENDIZAJE: C -> PYTHON\n")
    leccion_0_indentacion()
    leccion_1_memoria()
    leccion_2_estructuras()
    leccion_3_iteracion()
    leccion_4_excepciones()
    leccion_5_poo()
    
    print("\n¡Felicidades! Has completado el tour de conceptos base.")