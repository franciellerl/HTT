import terrestre

class Carro(terrestre.Terrestre):
    _cor = " "
    def __init__(self, nome, cor):
        super().__init__(nome)
        self._cor = cor
    def getcor(self):
        return self._cor
    def setcor(self, cor):
        self._cor = cor

    #def (e atributo cor) exclusivo dos carros
    def cor(self):
        print(f"O carro é {self._cor}")
