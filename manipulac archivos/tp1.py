#1
def cuantasNO(archivo, letra):
    suma=0
    with open(archivo, 'r') as miarch:
        for linea in miarch.read().split('\n'):
            if linea[0]!= letra:
                suma += 1

    print(suma)
#2
def primeraslineas(archivo, n):
    with open(archivo, 'r') as mi_arch:
        return mi_arch.readlines()[:n]
    print(primeraslineas())

#3
def guardar(archivo, lineas):
    lista=[]
    with open(archivo, 'r') as miarch:
        for elemento in miarch:
            lista.append(elemento)
    print(lista[-lineas:])    

#4

def contar(archivo):
    with open(archivo, "r") as aerchevo:
        lista_palabras = aerchevo.read().split()
        print(len(lista_palabras))

#5
def sustituto(archivo1, archivo2):
    with open(archivo1, "r") as f, open(archivo2, "w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write(letra.replace(letra, letra + "\n"))

#6
def eliminar(archivo1, archivo2):
    with open(archivo1, "r") as f, open(archivo2, "w") as a:
        for linea in f.read():
            a.write(linea.strip("\n"))

#7
def palabra_larga(archivo):
    caracteres = 0
    palabra = ""
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > caracteres:
                caracteres = len(word)
                palabra = word
    return palabra, caracteres

#8
def pollo_vignolo(archivo1, archivo2, archivo3):
    with open(archivo1, "r") as f, open(archivo2, "r") as a, open(archivo3, "w") as af:
        for palabra in f.read():
            af.write(palabra.replace(archivo1, archivo3))
        for palabra in a.read():
            af.write(palabra.replace(archivo2, archivo3))

#9
def world_counter(archivo):
    frecuencias = {}
    with open(archivo, "r") as arc:
        word_list = arc.read().split()
        for palabra in word_list:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
        for word in frecuencias.keys():
            frecuencias[word] = round(frecuencias[word] / len(word_list),3)

#10
import glob
import os
def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as s:
        for f in lista_txt:
            file = open(f, "r")
            s.write(file.read())
            file.close()












        
