#13
import re
def reemplazar(str):
    return re.sub('\W','_', str, 2)

print(reemplazar('holaaaaaaa'))