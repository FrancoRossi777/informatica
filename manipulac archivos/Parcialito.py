import re
def cuantasveces(str):
    resultado=re.findall('bc9', str)
    return len(resultado)

def sin_c(str):
    return re.findall('aa([^c]*?)gg', str)
    #el ? favorece a los matches internos


#poo
class Auto():
    def __init__(self):
        self.consumo=0,5
        self.rpmm=0
        self.cambio=None #o 0

    def arrancar(self):
        self.cambio=1
        self.rpm=500

    def bajarcambio(self):
        if 