"""
Crear una función vacunacion que recibe una lista (que representa días del mes) con  diccionarios en donde se indica, para cada departamento, la cantidad de vacunas contra la gripe que fueron suministradas en ese día.

Por ejemplo, la lista [
    {“Montevideo”:100,“Maldonado”:20,“Canelones”:30},
    {“Montevideo”:150,“Maldonado”:40},
    {“Montevideo”:100,“Canelones”:15}
]

Indica que el día 1 se suministraron 100 vacunas en Montevideo, 20 en Maldonado y 30 en Canelones, el día 2 se suministraron 150 vacunas en Montevideo y 40 en Maldonado y el día 3 100 vacunas en Montevideo y 15 en Canelones.
Si para un día en particular no se suministraron vacunas entonces no figurará el departamento; siguiendo con el ejemplo, para el día 2 no se suministraron vacunas en Canelones.
La función vacunacion deberá crear un nuevo diccionario en donde para cada departamento se contabilice el total de vacunas recibidas, siguiendo con el ejemplo Montevideo debería reflejar las 350 vacunas en Montevideo, 60 en Maldonado y 35 en Canelones.
Finalmente el programa deberá escribir las líneas del diccionario en un archivo llamado vacunacion.txt, es decir en cada línea debe escribirse el nombre del departamento seguido de la cantidad de vacunas.
El programa deberá manejar excepciones al escribir el archivo (IOError), de forma de que el programa sea resiliente ante falta de espacio en disco o falta de permisos para guardar el archivo.
"""


def vacunation(vacunations_per_day):
    total_vacunations = {}
    for day in vacunations_per_day:
        for department in day:
            if department not in total_vacunations:
                total_vacunations[department] = day[department]
            else:
                total_vacunations[department] += day[department]

    return total_vacunations


def write_file(vacunation_data):
    try:
        text = "\n".join(
            [
                f"{department} {vacunations}"
                for (department, vacunations) in vacunation_data.items()
            ]
        )
        with open("vacunacion.txt", "w") as file:
            file.write(text)

    except IOError:
        print("Error al escribir el archivo")


vacunations_data = [
    {"Montevideo": 100, "Maldonado": 20, "Canelones": 30},
    {"Montevideo": 150, "Maldonado": 40},
    {"Montevideo": 100, "Canelones": 15},
]

result = vacunation(vacunations_data)
write_file(result)
