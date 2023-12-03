# problema4.py
import os

def menu_iterativo():
    try:
        while True:
            print("1. Dividir dos números")
            print("2. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    dividir_numeros_con_excepciones(num1, num2)
                except ValueError:
                    print("Error: Ingrese números válidos.")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    print(f"Directorio de trabajo: {os.getcwd()}")
            elif opcion == '2':
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    finally:
        print("Proceso terminado")

def dividir_numeros_con_excepciones(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        raise Exception("No se puede dividir por cero.")
    else:
        print(f"Resultado de la división: {resultado}")