class meioTransporte():
    _nome = " "
    def __init__(self, nome):
        self._nome = nome
    def getnome(self):
        return self._nome
    def setnome(self, nome):
        self._nome = nome

    #def mover() se mantém o mesmo em todas as classes
    def mover(self):
        print(f"O(A) {self._nome} está movendo")
      
    #def tipo() é sobrescrita em terrestre, aquatico(barco e remo) e aereo
    def tipo(self):
        print("Este é um Meio de Transporte")
