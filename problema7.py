# ... (código existente)

class Phone:
    def __init__(self, marca, modelo, memoria_ram, memoria_sd, duracion_bateria):
        # ... (atributos existentes)
        self.nivel_bateria = 100  # Por defecto, la batería comienza al 100%

    # ... (métodos existentes)

    def cambiar_duracion_bateria(self, nueva_duracion):
        """
        Cambia la duración de la batería del teléfono.
        """
        self.duracion_bateria = nueva_duracion

    def mostrar_nivel_bateria(self):
        """
        Muestra el nivel actual de la batería del teléfono.
        """
        print(f"Nivel de batería: {self.nivel_bateria}%")

# ... (código existente)