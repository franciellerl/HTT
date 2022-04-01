import meiotransporte

class Terrestre(meiotransporte.meioTransporte):
    def __init__(self, nome):
        super().__init__(nome)

    def tipo(self):
        print("Este é um Meio de Transporte Terrestre")
