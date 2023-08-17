# Calcular el factorial de un número N. Plantear la solución utilizando la
# estructura WHILE y la estructura FOR.


def factorial_for(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r


def factorial_while(n):
    r = 1
    i = 1
    while i <= n:
        r = r * i
        i += 1
    return r


print(f"El factorial de 5 es: {factorial_for(5)}")
print(f"El factorial de 5 es: {factorial_while(5)}")
