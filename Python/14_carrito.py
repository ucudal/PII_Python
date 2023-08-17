class Carrito:
    def __init__(self, usuario):
        self.usuario = usuario
        self.productos = {}

    # Agrega un producto y su cantidad
    def agregar(self, producto, cantidad):
        self.productos[producto] = cantidad

    # Obtiene la cantidad total de productos
    def cantidad_total(self):
        cantidad = 0
        for clave in self.productos:
            cantidad += self.productos[clave]
        return cantidad

    def __str__(self):
        return f"Usuario: {self.usuario}"

    # Vacía el carrito
    def vaciar(self):
        self.productos = {}

    # Obtiene el monto a pagar
    def total_a_pagar(self):
        total = 0
        for clave in self.productos:
            total += self.productos[clave] * clave.precio
        return total

    # permite verifica si el carrito está vacío
    def esta_vacio(self):
        return len(self.productos) == 0


class Juguete:
    def __init__(self, nombre, precio):
        self.nombre_juguete = nombre
        self.precio = precio


class Ropa:
    def __init__(self, tipo, color, precio):
        self.tipo = tipo
        self.color = color
        self.precio = precio


if __name__ == "__main__":
    carrito = Carrito("Andrés")
    ropa1 = Ropa("Camiseta", "Rojo", 19.99)
    ropa2 = Ropa("Pantalón", "Azul", 29.99)
    juguete = Juguete("Pelota", 9.99)

    carrito.agregar(ropa1, 2)
    carrito.agregar(ropa2, 1)
    carrito.agregar(juguete, 1)

    print(carrito)
    print(f"Cantidad de productos en el carrito: {carrito.cantidad_total()}")
    print(f"Monto total a pagar: {carrito.total_a_pagar()}")

    carrito.vaciar()
    print(f"El carrito está vacío: {carrito.esta_vacio()}")
