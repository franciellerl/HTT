class imovel:
    id = ""
    lougradouro = ""
    cep = ""
    bairro = ""
    cidade = ""

    def __repr__(self): 
        return "ID:%s lougradouro:%s cep:%s bairro:%s cidade:%s" % (self.id, self.lougradouro, self.cep, self.bairro, self.cidade)

    def getid(self):
        return self.id
    def setid(self, id):
        self.id = id

    def getlougradouro(self):
        return self.lougradouro
    def setlougradouro(self, lougradouro):
        self.lougradouro = lougradouro

    def getcep(self):
        return self.cep
    def setnome(self, cep):
        self.cep = cep

    def getbairro(self):
        return self.bairro
    def setnome(self, bairro):
        self.bairro = bairro

    def getcidade(self):
        return self.cidade
    def setnome(self, cidade):
        self.cidade = cidade