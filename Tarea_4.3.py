numeros = int(input("Ingresar cantidad de numeros: "))
suma = 0
for valor in range(0,numeros,1):
    print("Ingrese el Numero ", valor+1)
    numero = int(input())
    suma = suma + numero
else:
    print("El promedio es = ",suma/numeros)