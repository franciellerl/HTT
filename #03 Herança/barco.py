import aquatico

class Barco(aquatico.Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

    def tipo(self):
        print("Este é um Barco")
