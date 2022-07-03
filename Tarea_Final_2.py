from datetime import date
from datetime import datetime
from email import message
from tkinter import N
class estudiantes():
    #Contructor
    def __init__(self, matricula,nombre,apellido,fecha_nacimiento,examenes,notaFinal ):
        #Atributos
        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.examenes = examenes
        self.notaFinal = notaFinal
    
    #Metodos 
    def __str__(self):
        return f" Matricula: {self.matricula}\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Nota Final: {self.notaFinal} Nota: {self.examenes}"
    def __getitem__(self,pos):
        return self.examenes[pos]
    def busqueda(self,matricula):
        return matricula
    def __setitem__(self,pos,value):
        self.examenes[pos] = value
    def listarExamenes(self):
        return f"Nota: {self.examenes}\nNota Final: {self.notaFinal}"
    def getEdad():
        pass
    def filtroFechas(self,fecha_desde):
        for dicc in self.examenes.values():
            if dicc["fecha"] == fecha_desde:
                longitud = len()
    def perfilEstudiante(self):
        print(f"Matricula: {self.matricula}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNota Final: {self.notaFinal}")
        print(self.listarExamenes())




def cargar_examen():
    nota_aux = 0
    fecha_aux = 0
    cont = 1
    examenes = {}
    cantidad_examenes = int(input("Cuantos examenes desea cargar: \n >>>"))
    for __ in range(cantidad_examenes):
        examen = {"nota":"","fecha":""}
        
        #Carga de examen
        nota = float(input(f"Ingresar nota:"))
        examen["nota"] = nota

        #Ingreso de Fecha en formato dateTime
        opcion = input("¿Desea cargar la fecha actual? si/no:\n >>>").lower()
        if opcion == "si":
            fecha = today = date.today()
            examen["fecha"] = fecha
        else:
            fecha_aux = input("Ingresar Fecha formato DD-MM-AAAA:")
            lista_fecha = fecha_aux.split("-")
            fecha = datetime(int(lista_fecha[2]),int(lista_fecha[1]),int(lista_fecha[0]))
            examen["fecha"] = fecha
        examenes[str(cont)] = examen
        cont += 1
    return examenes
        



lista_estudiantes = []

def registrarEstudiantes():
    d1 = input(f"Ingresar matricula:")
    d2 = input(f"Ingresar nombre:")
    d3 = input(f"Ingresar apellido:")
    d4 = input(f"Ingresar fecha de nacimiento DD-MM-AAAA:")
    d5 = cargar_examen()
    promedio = 0
    for nota in d5:
        n = d5[nota]["nota"]
        promedio += n
    d6 = promedio/len(d5)
    print(d6)
    estudiante = estudiantes(d1,d2,d3,d4,d5,d6)
    lista_estudiantes.append(estudiante)


def listadoEstudiantes():
    for estudiante in lista_estudiantes:
        print(estudiante)
        print("------------")

def buscarEstudiante():
    m = input("Que matricula desea buscar: \n >>>")
    for estudiante in lista_estudiantes:  
        if m == estudiante.matricula:
            print("Se encontro el estudiante")
            return estudiante
    else:
        print("No se encontro")
        return None
    
def actualizarPromedio(estudiante):
    promedio = 0
    for clave in estudiante.examenes:
        n = estudiante.examenes[clave]["nota"]
        promedio += n
    estudiante.notaFinal = promedio/len(estudiante.examenes)

def modificarNotas():
    cont = 1
    estudiante = buscarEstudiante()
    if not (estudiante == None):
        fecha_examen = input("Ingresar fecha de examen a modificar formato dd-mm-aaaa:\n >>>")
        for clave in estudiante.examenes:
            aux = str(estudiante.examenes[clave]["fecha"])[0:10].split("-")
            fecha_objeto = aux[2]+"-"+aux[1]+"-"+aux[0]
            if fecha_objeto == fecha_examen:
                    print("Se encontro la fecha")
                    nota = int(input("Ingresar nota nueva: \n >>>"))
                    estudiante.examenes[clave]["nota"] = nota
                    actualizarPromedio(estudiante)
                    print("Nota actulizada con exito!!!")
                    return
            elif cont < len(estudiante.examenes):
               cont+=1
               continue
            else:
               print("No se encontro la fecha deseada!!!")
               return
    else: 
        return None


def listarMatriculas():
    lista_matriculas = []
    for estudiante in lista_estudiantes:
        lista_matriculas.append(estudiante.matricula)
    for matricula in lista_matriculas:
        print(matricula)

    
        

def filtrarExamenesEstudiante():
    estudiante = buscarEstudiante()
    if not (estudiante == None):
        fecha_desde = input("Ingresar fecha de inicio \n>>>")
        estudiante.filtroFechas(fecha_desde)
    else:
        print("No se encuentra el estudiante espesificado!!!")
def listarNotasEstudiante():
    estudiante = buscarEstudiante()
    print(estudiante.listarExamenes())

def fichaEstudiante():
    estudiante = buscarEstudiante()
    estudiante.perfilEstudiante()

def main():
    
    while True:
        print("BIENVENIDO AL REGISTRO ACADEMICO DE ESTUDIANTES")
        opcion = input("""Seleccione una opcion 
        1 - Registrar 
        2 - Listado
        3 - Buscar matricula
        4 - Modificar notas 
        5 - Listar matriculas
        6 - Listar notas 
        7 - Ficha estudiante
        8 - Salir
        >>>""")
        if opcion == "1":
            registrarEstudiantes()
     
        elif opcion == "2":
            listadoEstudiantes()
        elif opcion == "3":
            buscarEstudiante()
        elif opcion == "4":
            modificarNotas()
        elif opcion == "5":
            listarMatriculas()
        elif opcion == "6":
            listarNotasEstudiante()
        elif opcion == "7":
            fichaEstudiante()
        elif opcion == "8":
            print("Finalizo el programa")
            break  
        else:
            print("Opcion incorrecta")


#Aca arranca el programa
main()

