numeros = [1,3,6,9] 
numero = int(input("Ingresar un numero de 0 a 9 "))
validacion = 0
while numero >= 9 or numero <= 0:
      numero = int(input("Valor incorrecto ingresar nuevamente "))
else:
    
    for valor in numeros:
      if valor == numero:
          validacion = 1
            
    else:
        if  validacion == 1:
            print("Se encuentra en la lista")
        else:
            print("El numero no se encuentra en la lista")
