numero = int(input("Introducir un numero impar: "))

while numero%2 == 0:
    numero = int(input("No es impar, colocarlo de nuevo: "))
else: 
    print("El usuario ingreso un numero par")


