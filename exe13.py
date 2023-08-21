import math

class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def calculoArea(self):
        return math.pi*self.raio**2
    def calculoCircunferencia(self):
        return 2*math.pi*self.raio

circulo1 = Circulo(10)
print(circulo1.calculoArea())


class Cilindro(Circulo):
    def __init__ (self, raio, altura):
        super().__init__(raio)
        self.altura = altura
    
    def calculoVolume(self):
        return self.calculoArea()*altura

cilindro1 = Cilindro(10,4)

print(cilindro1.calculoVolume)
