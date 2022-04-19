sustituir=[" ", "_", ":"]
import re 
def reemplazar(string):
    return re.sun(sustituir,"|", string)

print(reemplazar('hola'))