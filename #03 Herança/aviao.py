import aereo

class Aviao(aereo.Aereo):
    _numAssentos = " "
    def __init__(self, nome, podeVoar, numAssentos):
        super().__init__(nome, podeVoar)
        self._numAssentos = numAssentos
    def getnumAssentos(self):
        return self._numAssentos
    def setnumAssentos(self, numAssentos):
        self._numAssentos = numAssentos

    #def (e atributo numAssentos) exclusivo dos aviôes
    def assentos(self):
        print(f"Este avião possui {self._numAssentos} assentos")
