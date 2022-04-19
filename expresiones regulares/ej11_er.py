import re
def empiezaconP(lista_str):
    return(re.findall('[^P]', lista_str))
lista1=["Practica Python", "Practica C++", "Practica Fortran"]
print(empiezaconP(lista1))