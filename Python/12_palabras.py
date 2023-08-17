
def buscar_palabras(frase: str, palabra: str):
    palabras = frase.split()
    posiciones = []

    # Recorrer lista de palabras por texto y posición
    for i, p in enumerate(palabras):
        if p == palabra:
            posiciones.append(i)

    return posiciones


if __name__ == '__main__':
    print(buscar_palabras("Hola Mundo", "Mundo"))
    print(buscar_palabras("Hola Mundo", "Python"))
    print(buscar_palabras("Primero resuelve el problema y luego escribe el código", "el"))
