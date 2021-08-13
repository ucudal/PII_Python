#Escribir una función que abra 2 archivos indicados por parámetro y escriba un nuevo
#archivo con las líneas intercaladas de los archivos originales.

def combine(file1, file2, file3):

    a1 = open(file1)
    a2 = open(file2)
    a3 = open(file3, "w")

    line1 = a1.readline()
    while (line1):
        line1 = line1.rstrip() # elimina el newline
        a3.write(line1 + "\n")

        line2 = a2.readline()
        if (line2):
            line2 = line2.rstrip() # elimina el newline
            a3.write(line2 + "\n")

        line1 = a1.readline()

    # Si el archivo2 es más grande hay que escribir las lineas
    # que quedaron sin leer
    line2 = a2.readline()
    while (line2):
        line2 = line2.rstrip()
        a3.write(line2 + "\n")
        line2 = a2.readline()

    a1.close()
    a2.close()
    a3.close()

# Programa principal
file1 = "archivo1.txt"
file2 = "archivo2.txt"
file3 = "archivo3.txt"

print("Intercalando el archivo: {} con el archivo: {}".format(
    file1, file2
))
print("y escribiendo el resultado en el archivo: {}".format(
    file3
))

combine(file1, file2, file3)

print()
print()

file4 = "archivo4.txt"

print("Intercalando el archivo: {} con el archivo: {}".format(
    file2, file1
))
print("y escribiendo el resultado en el archivo: {}".format(
    file4
))
combine(file2, file1, file4)
print()
