
x= int(input("Ingresar N° 1: "))
y= int(input("Ingresar N° 2: "))
z= int(input("Ingresar N° 3: "))

if x == y  and x == z:
    print("Todos son numeros iguales")
elif x == y or x == z or y == z:
    print("Tenemos 2 numeros iguales")
elif x != y and x !=z:
    print("Todos son distintos") 

