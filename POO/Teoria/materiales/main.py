#OBJETOS: entidad computacional->entiende mensajes
#POO: programacion a objetos-> muchos objetos q se comunican entre si
#cdo el objeto conoce o hace la operacion que le pedimos NO TIRA ERROR

from aves import pepita, anastasia, roberta #todos los estados se importan arriba
###print(pepita.cantar_boleros())
#pepita no sabe cantar boleros porque tira error
# lo que hacen los objetos se llaman atributos
# los mensajes se usan haciendo .mensaje()--> UN MENSAJE ES UN METODO

###print(pepita.comer_alpiste())-->erros, faltan gramos
###print(pepita.comer_alpiste(4))#4 gramos#OBJETOS: entidad computacional->entiende mensajes
#POO: programacion a objetos-> muchos objetos q se comunican entre si
#cdo el objeto conoce o hace la operacion que le pedimos NO TIRA ERROR

print(pepita.energia)
print(pepita.comer_alpiste(10))#desp de comer aumenta energia
print(pepita.energia)
print(pepita.volar_en_circulos())#desp de volar gasta energia (10)
print(pepita.energia)
print(pepita.comer_alpiste(1))
print(pepita.energia)#cada gramo le suma 4 de energia
#podra entender el argumento volar mas de una vez?
#print(pepita.volar_en_circulos(2))-->no porque tira error

#Los objetos pueden tener un estado, en el caso de pepita, su estado es la energia
#COMPORTAMIENTO DE LOS OBJETOS: cdo cambian de estado, en este caso cuando pepita tiene mas o menos energia

print(anastasia==pepita)#no son iguales, NO SON EL MIDMO OBJETO->LOWS OBJETOS TIENEN DISTINTAS IDENTIDADES
print(anastasia.energia)
print(anastasia)#tamb es una golondrina 
#GOLONDRINA es una CLASE, y anastasia y pepita son OBJETOS
#    L nos  da una idea de lo q pueden hacer los objetos de esa clase
#como forman parte de la misma clase es de esperar que haga lo mismo, quwe entiendan los mismos mensajes

print(anastasia.comer_alpiste(1))
print(anastasia.energia)#le da la misma energia
print(anastasia.volar_en_circulos())#desp de volar gasta energia (10)
print(anastasia.energia)#se cansan lo mismo
#SE COMPORTAN IGUAL EN ESTE CASO, la diferencia esta en su estado

print(roberta)
print(roberta.energia)
print(roberta.cantidad_dientes)
print(roberta.comer_peces(1))
print(roberta.energia)
print(roberta.volar_en_circulos())
print(roberta.energia)
#INTERFAZ de un obj->conjunto de mensajes q entiende
#roberta comparte parcialmente la interfaz con golondrinas, entiende el de volar en cirvulos, pero no el de comer alpiste

#class nombre de clase(EN MAYUSCULA): todos los mensajes q puede reconocer cada objeto
#un metodo funciona dentro de una clase, las funciones estan fuera de las clases
#los metodos siempren tienen el SELF como primer argumento-->def comer_alpiste(self, gramos):
#SELF: representa a un objeto dado
print(roberta.comer_peces(200))
print(roberta.energia)