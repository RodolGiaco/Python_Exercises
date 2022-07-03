import json  
ruta="C:/Users/rodol/Desktop/python-course/CursoPython"
encabezado = ["Matricula","Nombre","Edad"]
alumnos = {}
clave = {}
valores = {}
def agregar():
    matricula = input("Ingresar Matricula formato 000x:")
    nombre = input("Ingresar Nombre:")
    edad = int(input("Ingresar Edad:"))
    valores["nombre"] = nombre
    valores["edad"] = edad
    clave[matricula] = valores
    alumnos.update(clave)
    #print(alumnos)

while True:
    opcion = input("Desea agregar alumnos si/no: \n>>>").lower()
    if opcion == "si":
        agregar()
    else:
        print("Nos vemos!!!")
        archivo_json= open( ruta + "/diccionario.json","w")
        json.dump(alumnos,archivo_json,indent=4)
        archivo_json.close()
        break

