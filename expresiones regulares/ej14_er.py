#14
import re 
def reemplazar(str):
    return re.sub("\S", ";", str)

print(reemplazar('holsa'))