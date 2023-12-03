# problema5.py
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, year = self.codigo.split('-')
        return f"Producto: {self.nombre}, País: {pais}, Lote: {lote}, Año: {year}"