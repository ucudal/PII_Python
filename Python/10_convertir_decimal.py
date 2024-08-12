"""
Crear una función convertir_decimal que reciba una cadena numero y un entero base como parámetros y que devuelva el numero dada la base convertido en decimal.
Si numero no es válido según la base entonces devolverá -1.
 - Se da por entendido que numero será siempre positivo por lo que no deberá validarse.
 - Se da por entendido que la base será 2 o 16

Nota: No se puede utilizar ninguna función matemática de Python que convierta números de cualquier base a decimal, deberá programarse la solución.
"""

print(convert_decimal("11", 2))
print(convert_decimal("12", 2))
print(convert_decimal("101", 2))
print(convert_decimal("A", 16))
print(convert_decimal("G", 16))

def convert_decimal(number, base):
    result = 0
    while number:
        # Obtener valor numerico del digito
        digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(number[0].upper())

        # Verificar que el digito sea valido en la base dada
        if digit >= base:
            return -1

        # Calcular valor decimal del digito
        result += digit * base ** (len(number) - 1)
        number = number[1:]

    return result
