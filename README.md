![UCU](https://github.com/ucudal/PII_Conceptos_De_POO/raw/master/Assets/logo-ucu.png)
# Universidad Católica del Uruguay
## Facultad de Ingeniería y Tecnologías
### Programación II
Algunos ejercicios en Python vistos en el curso de Programación I para resolver en C#

Para ejecutar estos archivos en Visual Studio Code abrir la carpeta raíz del repositorio como espacio de trabajo y luego abrir cada archivo .py que quieran ejecutar. Sigan las instrucciones que les da Visual Studio Code para instalar los complementos necesarios para ejecutar programas Python.

### Ejercicio 10: convertir decimal

Crear una función `convertir_decimal` que reciba una cadena `numero` y un entero `base` como parámetros y que devuelva el numero dada la base convertido en decimal. Si numero no es válido según la base entonces devolverá -1.

Se da por entendido que numero será siempre positivo por lo que no deberá validarse.

Se da por entendido que la base será 2 o 16

Ejemplos:

- `convertir_decimal("11,2")` devolverá `3`

- `convertir_decimal("12",2)` devolverá `-1` pues no puede formarse el número 12 en base 2

- `convertir_decimal("100",2)` devolverá `5`

- `convertir_decimal("A",16)` devolverá `10`

- `convertir_decimal("G",16)` devolverá `-1` pues no puede formarse el número G en base 16

> **Nota** No se puede utilizar ninguna función matemática de Python que convierta números de cualquier base a decimal, deberá programarse la solución.

### Ejercicio 11: vacunación

Crear una función `vacunacion` que recibe una lista (que representa días del mes) con  diccionarios en donde se indica, para cada departamento, la cantidad de vacunas contra la gripe que fueron suministradas en ese día.

Por ejemplo, la lista
```python
[
{"Montevideo":100,"Maldonado":20,"Canelones":30},
{"Montevideo":150,"Maldonado":40},
{"Montevideo":100,"Canelones":15}
]
```
Indica que el día 1 se suministraron 100 vacunas en Montevideo, 20 en Maldonado y 30 en Canelones, el día 2 se suministraron 150 vacunas en Montevideo y 40 en Maldonado y el día 3 100 vacunas en Montevideo y 15 en Canelones.

Si para un día en particular no se suministraron vacunas entonces no figurará el departamento; siguiendo con el ejemplo, para el día 2 no se suministraron vacunas en Canelones.

La función `vacunacion` deberá crear un nuevo diccionario en donde para cada departamento se contabilice el total de vacunas recibidas, siguiendo con el ejemplo Montevideo debería reflejar las 350 vacunas en Montevideo, 60 en Maldonado y 35 en Canelones.

Finalmente el programa deberá escribir las líneas del diccionario en un archivo llamado `vacunacion.txt`, es decir en cada línea debe escribirse el nombre del departamento seguido de la cantidad de vacunas.

El programa deberá manejar excepciones al escribir el archivo (`IOError`), de forma de que el programa sea resiliente ante falta de espacio en disco o falta de permisos para guardar el archivo.

### Ejercicios 12: palabras

Crear una función `buscar_palabras` que reciba un string texto y un string palabra como parámetros y que devuelva una lista con las posiciones de palabra dentro de texto. En caso de no encontrar la palabra devolverá una lista vacía.

Ejemplos:

- `buscar_palabras("Hola Mundo","Mundo")` devolverá [1]

- `buscar_palabras("Hola Mundo","Python")` devolverá []

- `buscar_palabras("Primero resuelve el problema y luego escribe el código","el")` devolverá [2,7]


> **Nota** Es posible usa la función `split` de Python para obtener una lista de palabras.

### Ejercicio 13: bingo

Escribir una función que permite verificar si dado un cartón de Bingo y la lista de números sorteados, el jugador "tiene Bingo" (cartón lleno). El Bingo consiste en que un usuario tiene un cartón con filas de números y va marcando los números sorteados. El jugador gana cuando se hayan sorteado todos los números que están en su cartón.

La función recibe una lista que contiene listas que representan las filas de números correspondientes al cartón y una lista con los números sorteados. Deberá devolver `True` en caso que tenga Bingo o `False` en caso contrario.

Ejemplos:

- `tiene_bingo( [[2,12,33,45,67], [5,23,45,77,86], [3,34,46,56,88,97]], [1,2,3,5,10, 12,23,33,34,45,46,56,67,68,69,75,76,77,80,85,86,87,88,96,97])` devuelve `True`
- `tiene_bingo( [[2,12,33,45,67], [5,23,45,77,86], [3,34,46,56,88,97]], [1,2,3,5,10, 12,23,33,34,45,46,56,67,68,69,75,76,77,80,85,86,87,88,96])` devuelve `False`

> **Nota** La función debe ser capaz que funcionar en cartones de cualquier dimensión

### Ejercicio 14: carrito

Se pide crear un objeto `Carrito`, al cual se le deben agregar los siguientes objetos.

- 2 `Juguetes` distintos

- 1 `Ropa`

Imprimir por pantalla la cantidad total de productos en el carrito y el total a pagar.

Vaciar el carrito y verificar que está vacío.