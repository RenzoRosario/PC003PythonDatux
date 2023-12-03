class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = input("Ingrese la edad: ")
        self.direccion = input("Ingrese la dirección: ")

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}"

# Uso de la clase Persona
if __name__ == "__main__":
    persona = Persona()
    print(persona)
