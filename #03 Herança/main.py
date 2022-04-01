import carro, caminhao, remo, barco, aviao, helicoptero

#Fazer a herança das seguintes classes:
#MeioTransporte
#Terrestre            / Aquatico           / Aereo
#Carro / Caminhao     Remo / Barco       Avião / Helicóptero
#Use a imaginação para criar e separar os seus atributos
#Para o dia 07/04

#Carro
car = carro.Carro("fiat uno", "azul")
car.mover()
car.tipo()
car.cor()
print("\n")

#Caminhao
cami = caminhao.Caminhao("carreta", "arroz")
cami.mover()
cami.tipo()
cami.carga()
print("\n")

#Remo
remar = remo.Remo("skiff")
remar.mover()
remar.tipo()
print("\n")

#Barco
barca = barco.Barco("iate")
barca.mover()
barca.tipo()
print("\n")

#Aviao
ave = aviao.Aviao("airbus 380", True, 33)
ave.mover()
ave.tipo()
ave.voa()
ave.assentos()
print("\n")

#Helicoptero
heli = helicoptero.Helicoptero("bell 429", False, True)
heli.mover()
heli.tipo()
heli.voa()
heli.militar()
print("\n")
