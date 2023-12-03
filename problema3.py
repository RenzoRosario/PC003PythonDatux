class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class CatalogoProductos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Producto: {producto.nombre}, Código: {producto.codigo}")