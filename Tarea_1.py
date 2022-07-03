nota1 = int(input("Ingrese la nota del 1° examen: "))
nota2 = int(input("Ingrese la nota del 2° examen: "))

notaFinal = nota1*0.40 + nota2*0.60
if notaFinal >= 7:
    print("Alumno aprobo con:", notaFinal) 
else: print("Alumno desaprobo con:",notaFinal)





