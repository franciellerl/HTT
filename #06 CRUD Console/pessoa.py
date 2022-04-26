class pessoa:
    id = ""
    nome = ""
    datanasc = ""

    def __repr__(self): 
        return "ID:%s nome:%s datanasc:%s" % (self.id, self.nome, self.datanasc)

    def getid(self):
        return self.id
    def setid(self, id):
        self.id = id
    
    def getnome(self):
        return self.nome
    def setnome(self, nome):
        self.nome = nome

    def getdatanasc(self):
        return self.datanasc
    def setid(self, datanasc):
        self.datanasc = datanasc
    
