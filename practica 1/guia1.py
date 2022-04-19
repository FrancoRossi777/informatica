import re
from turtle import title


def longitud(string):
    return len(string)

print (longitud('hola'))

#2
def letra56(palabra):
    return str.upper(palabra[4])+str.upper(palabra[5])

print (letra56('putamadre'))

#3
def saludo(nombre):
    return 'Hola'+ ' ' +nombre
print (saludo('juan carlos'))

#4 
def mayus(nombre):
    return nombre.title()

print (mayus('juan carlos'))

#6
def horasyminutos(minutos):
    return str(minutos//60) + ':' +str(minutos%60)

print (horasyminutos(150))

#5
def promedio(num1, num2, num3):
    return (num1+num2+num3)/3
print (promedio(2, 2, 2))

#7

def ejer7(sueldo_base):
    comision = 0.1 * sueldo_base * 4
    return "Extra:" + str(comision) + " Total:" + str(comision + sueldo_base)
print(ejer7(100))

#8 
#respuestas = input('respuesta1: '), input('respuesta2: '), input('respuesta3: ')
#notas=0
#for respuesta in respuestas:
    #if respuesta=='correcta':
        #notas += 4
    #elif respuesta=='incorrecta':
        #notas -= 1
    #elif respuesta=='':
        #notas += 0



#GUIA2

#1
def esmayomin(palabra):
    if palabra[0].isupper():
        return 'Mayúscula'
    else:
        return 'Minúscula'
print(esmayomin('ola'))

#2
def posoneg(numero):
    if numero%2==0 and numero>0:
        return 'NUmero par y positivo'
    elif numero%2==0 and numero<0:
        return 'NUmero par y negsativo'
    elif numero%2!=0 and numero>0:
        return 'Numero impar y positivo'
    elif numero%2!=0 and numero<0:
        return 'Numero impar y negativo'
    elif numero==0:
        return '0 y par'
print(posoneg(9))
#3
def dado(numero):
    if 1<=numero<=6:
        return 7-numero
    else:
        return 'Numero ingresado incorrecto'
print(dado(4))
#4 
def transpinternac(continente, peso):
    if peso>5:
        return 'entrega rechazada'
    elif continente=='América del Sur':
        return peso*10
    elif continente=='América central':
        return peso*15
    elif continente=='América del Norte':
        return peso*18
    elif continente=='Europa':
        return peso*24
    elif continente=='Asia':
        return peso*30
print(transpinternac('Asia', 2))

#5
def dia_semana(numero):
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miercoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sabado")
    elif numero == 7:
        print("Domingo")
    else:
        print("El numero es incorrecto")
print(dia_semana(3))

#6
lista='hola'
lista2= lista[::-1]
print(lista2)

#7
lista= input('el1: '), input('el2: '), input('el3: '), input('el4: ')
lista1=[]
for elementos in lista:
    if int(elementos)>=0:
        lista1+=elementos
    if int(elementos)<0:
        print(lista1)

#8
lista1=[1, 2, 3, 4, 5]
lista2=[1, 2, 3, 4, 5]
lista3=[lista1[0]+lista2[0], lista1[1]+lista2[1], lista1[2]+lista2[2], lista1[3]+lista2[3], lista1[4]+lista2[4]]
print(lista3)

#9


#10


















    
