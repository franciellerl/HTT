import terrestre

class Caminhao(terrestre.Terrestre):
    _tipoCarga = " "
    def __init__(self, nome, tipoCarga):
        super().__init__(nome)
        self._tipoCarga = tipoCarga
    def gettipoCarga(self):
        return self._tipoCarga
    def settipoCarga(self, tipoCarga):
        self._tipoCarga = tipoCarga

    #def (e atributo tipoCarga) exclusivo dos caminhoes
    def carga(self):
        print(f"O caminhão leva {self._tipoCarga}")
