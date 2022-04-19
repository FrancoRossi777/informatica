#15
import re
def esmailvalido(mail):
    if re.match("^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$", mail.lower()):
        print("Correo Incorrecto")
    else:
        print("Correo Correcto") 
print(esmailvalido(f.rossi.1102@gmail.com))   
