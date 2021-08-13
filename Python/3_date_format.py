#Escribir una función que recibe una cadena de caracteres como parámetro
#con una fecha de la forma “dd/mm/aaaa” y devuelve la fecha en formato
#“aaaa­‐mm­‐dd”.
#Ej.: 10/11/1977  1977­‐11­‐10
#No se debe utilizar la función split de Python.

def date_format(cadena):
    return cadena[6:]+"-"+cadena[3:5]+"-"+cadena[:2]

test_date="10/11/1977"
print("{} se convierte a: {}".format(test_date,date_format(test_date)))