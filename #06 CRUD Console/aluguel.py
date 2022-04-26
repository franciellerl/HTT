import imovel, proprietario

class aluguel(imovel.imovel, proprietario.proprietario):
    num_contrato = ""
    idImovel = ""
    idProp = ""

    def __repr__(self): 
        return "ID:%s num_contrato:%s IDImovel:%s IDProp:%s" % (self.id, self.num_contrato, self.idImovel, self.idProp)

    def getnum_contrato(self):
        return self.num_contrato
    def setid(self, num_contrato):
        self.num_contrato = num_contrato

    def getidImovel(self):
        return self.idImovel
    def setid(self, idImovel):
        self.idImovel = idImovel

    def getidProp(self):
        return self.idProp
    def setid(self, idProp):
        self.idProp = idProp
