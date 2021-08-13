#Implementar la diferencia simétrica de dos listas. La diferencia simétrica consiste en
#todos los elementos de la primera lista que no están en la segunda y de todos los
#elementos de la segunda lista que no están en la primera.
#Por ejemplo symdif([1, 2, 3], [3, 4, 5]) devuelve [1, 2, 4, 5]. El resultado no debe tener
#duplicados.

def symdiff(list1,list2):
    diferencia = []
    for elemento in list1:
        if elemento not in list2:
            diferencia.append(elemento)
    for elemento in list2:
        if elemento not in list1:
            diferencia.append(elemento)
    return diferencia

print(symdiff([1, 2, 3], [3, 4, 5]))
