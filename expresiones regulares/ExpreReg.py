import re

def verificar(str):
    return bool(re.search('[\w]', str))
print(verificar('Franco'))

def caracter_permitido1(string):
    resultado = True
    for caracter in string:
        if not bool(re.findall("\w", caracter)):
            return False
        else:
            return resultado
print(caracter_permitido1('{k'))

def tiene(string):
    return bool(re.search("he{2,3}", string))
print(tiene('heeermoso'))

def unidas(string):
    return re.findall('\D\w*_\D\w*', string)

print(unidas('hola como_estas'))

def empezar(numero, string):
    return bool(re.match(str(numero), string))

def encontrar(lista, frase):
    return bool(re.search(frase, str(lista)))
listaa=['vamo', 'juga', 'animal']
print(encontrar(listaa, 'vamo a juga animal de la vida'))

def encuentre(string):
    return re.findall('\w+\s+\w+', string)
print(encuentre('----hi lo.'))

def numericos(string):
    return re.findall('\d+', string)
print(numericos('tengo 19 años'))

def entreguiones(string):
    return re.findall('-(.*?)-', string)
print(entreguiones('hola-como-estas -oko-'))


def substrings(string):
    return re.search('(@|&)(.*?)(@|&)', string).group()

print(substrings('LA @ mpo & m'))


               
    
