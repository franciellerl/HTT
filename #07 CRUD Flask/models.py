from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:senha123@localhost:5432/crud_htt"
#postgresql://{seu_usuario}:{sua_senha}@{maquina_do_postgres}:{porta}/{banco_postegres}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class inquilino(db.Model):
    __tablename__ = 'inquilino'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class proprietario(db.Model):
    __tablename__ = 'proprietario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class imovel(db.Model):
    __tablename__ = 'imovel'

    id = db.Column(db.Integer, primary_key=True)
    lougradouro = db.Column(db.String())
    cep = db.Column(db.String())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())

    def __init__(self, lougradouro, cep, bairro, cidade):
        self.lougradouro = lougradouro
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
    
class aluguel(db.Model):
    __tablename__ = 'aluguel'

    id = db.Column(db.Integer, primary_key=True)
    num_contrato = db.Column(db.Integer)
    idImovel = db.Column(db.Integer, db.ForeignKey(imovel.id))
    idProp = db.Column(db.Integer, db.ForeignKey(proprietario.id))

    def __init__(self, num_contrato):
        self.num_contrato = num_contrato
        #self.idImovel = idImovel
        #self.idProp = idProp
