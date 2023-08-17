#Ejemplo manejo de excepciones

def basic_errors():
    y = 0
    x = [5, 3, 25, 100, ""]
    print(x)
    for i in range(len(x)):
        try:
            a = int(x[i + 1])
            print(a / y)
        except ValueError:
            print("Error de valor")
        except IndexError:
            print("Error de indice")
        except ZeroDivisionError:
            print("División por cero")
            y = 2
        finally:
            print("Fin iteracion: ", i + 1)

basic_errors()
