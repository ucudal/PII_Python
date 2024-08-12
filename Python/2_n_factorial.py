# Calcular el factorial de un número N. Plantear la solución utilizando la
# estructura WHILE y la estructura FOR.


def factorial_for(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result


def factorial_while(number):
    result = 1
    i = 1
    while i <= number:
        result = result * i
        i += 1
    return result


print(f"El factorial de 5 es: {factorial_for(5)}")
print(f"El factorial de 5 es: {factorial_while(5)}")
