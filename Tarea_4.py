num1, num2 = int(input("Ingresar Numero 1: ")), int(input("Ingresar numero 2: "))
opcion = 0

while opcion != 4:

        print("1)_Calcular la suma")
        print("2)_Calcular la resta")
        print("3)_Calcular multiplicacion")
        print("4)_Salir")

        opcion = int(input())  #Aca se frena el programa
        if opcion == 1:
            suma = num1 +num2
            print("Suma = ",suma)
          
        elif opcion == 2:   
            resta = num1 -num2
            print("Suma = ",resta)
            
        elif opcion == 3:   
            mult = num1*num2
            print("Suma = ",mult)

        elif opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
            print("Opcion invalida, volver a seleccionar")
else: 
    print("Usted a salido del programa")
 
    

    



