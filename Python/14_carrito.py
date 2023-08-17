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
