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

