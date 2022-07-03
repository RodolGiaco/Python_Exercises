#LINK DE GOOGLE COLABORATORY
#https://colab.research.google.com/drive/190B7yd0MKHA7N2Ncd6KMt9bodelGgRvK?usp=sharing 
def anio_bisiesto(anio):
  aux = str(anio)
  anio_secular = aux[2:]
  if type(anio) == int:
     if anio%4==0 and not(anio%100==0) or anio_secular == "00" and (anio%400==0):
        print("El año es bisiesto")
     else:
        print("El año no es bisiesto")
  else: 
    print("Ingresar un entero!!!")

anio_bisiesto(anio = int(input("Ingresar año bisiesto: ")))