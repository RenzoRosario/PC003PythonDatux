# main.py
from problema2 import Problema2
from problema3 import CatalogoProductos, Producto
from problema4 import menu_iterativo
from problema5 import Producto as ProductoEstructurado
from problema8 import Persona

if __name__ == '__main__':
    # 2. Calcular área del círculo de radio "r"
    Problema2().resolver_problema()

    # 3. Crear Catálogo de productos y agregar un producto
    catalogo = CatalogoProductos()
    producto = Producto("Aceite de motor", "ENGINE-01012023")
    catalogo.agregar_producto(producto)
    catalogo.mostrar_productos()

    # 4. Menú iterativo con opciones importadas
    menu_iterativo()

    # 5. Crear y mostrar un ProductoEstructurado
    producto_estructurado = ProductoEstructurado("Llanta", "PERU-6552-2023")
    print(producto_estructurado)

    # 6. Manejo de errores al dividir números
    try:
        dividir_numeros_con_excepciones(10, 2)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Directorio de trabajo: {os.getcwd()}")
    finally:
        print("Proceso terminado")
    
    # 8. Crear una clase Persona
    persona = Persona()
    print(persona)