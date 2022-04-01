import meiotransporte

class Aereo(meiotransporte.meioTransporte):
    _podeVoar = None
    def __init__(self, nome, podeVoar):
        super().__init__(nome)
        self._podeVoar = podeVoar
    def getpodeVoar(self):
        return self._podeVoar
    def setpodeVoar(self, podeVoar):
        self._podeVoar = podeVoar

    def tipo(self):
        print("Este é um Meio de Transporte Aereo")

    #def (e atributo podeVoar) exclusivo dos aereos
    def voa(self):
      if (self._podeVoar == True):
         print("Este transporte está habilitado para voar")
      else:
        print("Este transporte não está habilitado para voar")
