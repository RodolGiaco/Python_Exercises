nombre = input("Ingresar Nombre: ")
edad = int(input("Ingresar Edad: "))
validacion= (nombre != "Ariel") and (10 < edad < 25) and (len(nombre) >= 3 and len(nombre) < 10) and (edad * 4 > 40)
print("Acceso:",validacion)