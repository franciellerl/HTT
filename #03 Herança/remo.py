import aquatico

class Remo(aquatico.Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

    def tipo(self):
        print("Este é um Remo")
