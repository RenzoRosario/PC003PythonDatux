import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Problema2:
    def resolver_problema(self):
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        print("El área del círculo es: {:.2f}".format(area))