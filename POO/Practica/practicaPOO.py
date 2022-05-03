class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
#interfax:comer acariciar y estadebil, estado:cariias alinmento

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    def descuento(self, numero):
        return self.precio - ((numero*self.precio)/100)
compu=Notebook('HP', 'x', 100) 
print(compu.descuento(25))

class Contador:
    def __init__(self, valor):
        self.valor=valor
        self.ultimo=''
    def inc(self):
        self.valor+=1
        self.ultimo='incremento'
    def dis(self):
        self.valor-=1
        self.ultimo='disminución'
    def reset(self):
        self.valor=0
        self.ultimo='reset'
    def valorActual(self):
        print(self.valor)
        self.ultimo='actualización'
    def valorNuevo(self, nuevoValor):
        self.valor=nuevoValor
        self.ultimo='actualizacion'
    def ultimoComando(self):
        print(self.ultimo)
contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
contador.ultimoComando()

class Calculadora:
    def __init__(self):
        self.numero=0
    def cargar(self, num):
      self.num=num  
    def sumar(self, num):
        self.numero+=num
    def restar(self, num):
        self.numero-=num
    def multiplicar(self, num):
        self.numero*=num
    def valorActual(self):
        print(self.numero)

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()

class Gorriones:
    def