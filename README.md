<img alt="UCU" src="https://www.ucu.edu.uy/plantillas/images/logo_ucu.svg"
width="150"/>

# Universidad Católica del Uruguay

## Facultad de Ingeniería y Tecnologías

### Programación II

# Python a C#

## Objetivo

Resolver en C# algunos ejercicios en Python vistos en el curso de Programación I.

Para ejecutar estos archivos en Rider abrir la carpeta raíz del repositorio.
Rider nos avisará que la carpeta tiene una solución `Python.sln` y le diremos
que la queremos abrir. Luego ejecutan tanto el código en Python como en C# como
hicieron en el ejericio [Pasando de Programación I a Programación
II](https://github.com/ucudal/PII_P1_a_P2).

## Rúbrica corrección

La corrección de este ejercicio se hará entre pares usando la siguiente rúbrica:

<table>
  <tr>
    <th width="20%">Ítem a evaluar</th>
    <th width="20%">Perfecto</th>
    <th width="20%">Bien</th>
    <th width="20%">Mejorable</th>
    <th width="20%">Mal</th>
  </tr>
  <tr>
    <td>Funciona en C# igual que Python</td>
    <td colspan="3">El programa hace lo mismo</td>
    <td>El programa no hace lo mismo</td>
  </tr>
  <tr>
    <td>Convenciones en C#</td>
    <td>Sigue las convenciones de código</td>
    <td colspan="2">Sigue algunas convenciones de código</td>
    <td>No sigue las convenciones de código</td>
  </tr>
  <tr>
    <td>Estructuras de control condicional o repetición condicional</td>
    <td>La estructura es la más adecuada</td>
    <td colspan="2">La estructura fuciona pero no es la más adecuada</td>
    <td>La estructura de control no es la adecuada</td>
  </tr>
</table>

## Ejercicio 1: año bisiesto

Crear una función que determine si un año es bisiesto o no.

## Ejercicio 2: factorial

Crear una función que calcule el factorial de un número usando las estructuras
de control condicional `for` y `while`.

## Ejercicio 3: date format

Escribir una función que recibe una cadena de caracteres como parámetro con una
fecha de la forma “dd/mm/aaaa” y devuelve la fecha en formato “aaaa­‐mm­‐dd”.

Ejemplo: 10/11/1977 -> 1977­‐11­‐10

> [!NOTE]
> No se debe utilizar el método `string.Split()`.

## Ejercicio 5: sym diff

Implementar la diferencia simétrica de dos listas. La diferencia simétrica
consiste en todos los elementos de la primera lista que no están en la segunda y
de todos los elementos de la segunda lista que no están en la primera.

Por ejemplo symdif([1, 2, 3], [3, 4, 5]) devuelve [1, 2, 4, 5]. El resultado no
debe tener duplicados.

## Ejercicio 10: convertir decimal

Crear una función `convertir_decimal` que reciba una cadena `numero` y un entero
`base` como parámetros y que devuelva el numero dada la base convertido en
decimal. Si numero no es válido según la base entonces devolverá -1.

Se da por entendido que numero será siempre positivo por lo que no deberá
validarse.

Se da por entendido que la base será 2 o 16

Ejemplos:

- `convertir_decimal("11,2")` devolverá `3`

- `convertir_decimal("12",2)` devolverá `-1` pues no puede formarse el número 12
  en base 2

- `convertir_decimal("100",2)` devolverá `5`

- `convertir_decimal("A",16)` devolverá `10`

- `convertir_decimal("G",16)` devolverá `-1` pues no puede formarse el número G
  en base 16

> [!NOTE]
> No se puede utilizar ninguna función matemática de Python que convierta
> números de cualquier base a decimal, deberá programarse la solución.

## Ejercicios 12: palabras

Crear una función `buscar_palabras` que reciba un string texto y un string
palabra como parámetros y que devuelva una lista con las posiciones de palabra
dentro de texto. En caso de no encontrar la palabra devolverá una lista vacía.

Ejemplos:

- `buscar_palabras("Hola Mundo","Mundo")` devolverá [1]

- `buscar_palabras("Hola Mundo","Python")` devolverá []

- `buscar_palabras("Primero resuelve el problema y luego escribe el
  código","el")` devolverá [2,7]

> [!NOTE]
> Es posible usa la función `split` de Python para obtener una lista de
> palabras.

## Ejercicio 13: bingo

Escribir una función que permite verificar si dado un cartón de Bingo y la lista
de números sorteados, el jugador "tiene Bingo" (cartón lleno). El Bingo consiste
en que un usuario tiene un cartón con filas de números y va marcando los números
sorteados. El jugador gana cuando se hayan sorteado todos los números que están
en su cartón.

La función recibe una lista que contiene listas que representan las filas de
números correspondientes al cartón y una lista con los números sorteados. Deberá
devolver `True` en caso que tenga Bingo o `False` en caso contrario.

Ejemplos:

- `tiene_bingo( [[2,12,33,45,67], [5,23,45,77,86], [3,34,46,56,88,97]], [1,2,3,5,10, 12,23,33,34,45,46,56,67,68,69,75,76,77,80,85,86,87,88,96,97])` devuelve `True`
- `tiene_bingo( [[2,12,33,45,67], [5,23,45,77,86], [3,34,46,56,88,97]], [1,2,3,5,10, 12,23,33,34,45,46,56,67,68,69,75,76,77,80,85,86,87,88,96])` devuelve `False`

> [!NOTE]
> La función debe ser capaz que funcionar en cartones de cualquier dimensión

## Ejercicio 14: carrito

Se pide crear un objeto `Carrito`, al cual se le deben agregar los siguientes objetos.

- 2 `Juguetes` distintos

- 1 `Ropa`

Imprimir por pantalla la cantidad total de productos en el carrito y el total a pagar.

Vaciar el carrito y verificar que está vacío.
