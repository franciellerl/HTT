import aereo

class Helicoptero(aereo.Aereo):
    _ehMilitar = None
    def __init__(self, nome, podeVoar, ehMilitar):
        super().__init__(nome, podeVoar)
        self._ehMilitar = ehMilitar
    def getehMilitar(self):
        return self._ehMilitar
    def setehMilitar(self, ehMilitar):
        self._ehMilitar = ehMilitar

    #def (e atributo ehMilitar) exclusivo dos helicopteros
    def militar(self):
      if (self._ehMilitar == True):
         print("Este helicóptero é militar")
      else:
        print("Este helicóptero é civil")
