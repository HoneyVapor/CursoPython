# De C a Python
---

## 1. Adaptación: De C a la "Filosofía Python"

En C controlas todo; en Python, confías en el lenguaje. Tu primer paso es entender cómo Python maneja lo que ya conoces.

* **Tipado Dinámico vs. Estático:** Entender que en Python las variables son etiquetas a objetos, no cajas de memoria con un tamaño fijo.
* **Gestión de Memoria:** Olvida el `malloc` y `free`. Aprende cómo funciona el **Garbage Collector** y el conteo de referencias.
* **Identación Obligatoria:** En Python, el espacio en blanco es sintaxis, no solo estética.

## 2. Estructuras de Datos Nativas (El Corazón de Python)

En C, crear una lista enlazada o un hash map requiere esfuerzo. En Python, son ciudadanos de primera clase.

* **Listas y Tuplas:** Diferencia entre mutabilidad e inmutabilidad.
* **Diccionarios (Dicts) y Conjuntos (Sets):** Implementaciones de tablas hash extremadamente optimizadas.
* **List Comprehensions:** La forma "Pythonic" de transformar datos sin usar bucles `for` tradicionales de estilo C.

## 3. Programación Orientada a Objetos (POO)

C es procedimental; Python es profundamente orientado a objetos (todo es un objeto, incluso los números).

* **Clases y Objetos:** Uso de `self` (similar al puntero `this` en otros lenguajes).
* **Métodos Dunder (Mágicos):** Como `__init__`, `__str__` o `__add__`, que permiten sobrecargar operadores.
* **Herencia y Mixins:** Cómo estructurar código reutilizable.

## 4. El Ecosistema y Manejo de Entornos

Como Python depende de muchas librerías externas, saber gestionar tu espacio de trabajo es vital para no romper el sistema operativo.

* **PIP:** El gestor de paquetes.
* **Entornos Virtuales (`venv` o `conda`):** Crear "burbujas" aisladas para cada proyecto.
* **Módulos y Paquetes:** Cómo organizar archivos `.py` para que se comuniquen entre sí.

## 5. Bibliotecas Estándar y Especialización

Una vez domines el lenguaje, elige un camino según tus intereses:

| Camino | Librerías Clave |
| --- | --- |
| **Ciencia de Datos** | Pandas, NumPy, Matplotlib. |
| **Desarrollo Web** | Django o FastAPI. |
| **Automatización** | Selenium, Beautiful Soup, OS. |
| **IA / ML** | PyTorch, Scikit-learn, TensorFlow. |

---

### Un consejo de "C-boy" a "Pythonista"
No intentes escribir C en Python. Si ves que estás usando muchos índices en un bucle (`for i in range(len(lista))`), probablemente haya una forma más limpia de hacerlo usando **iteradores**.