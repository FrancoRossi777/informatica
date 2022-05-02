#15
import re

def esmailvalido(mail):
    if re.findall('[\W]+[-_\.]*[\W]+@[a-z]{1-9}\.[a-z]{2-4}', mail):
        print('correo correcto')
    else:
        print('correo incorrecto')
print(esmailvalido('hola@gmail.com'))