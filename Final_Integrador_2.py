#EJERCICIO 1
#https://colab.research.google.com/drive/1THzUL4M_FuLczsSiNS4PU2ZrqfH7iAVv?usp=sharing

#EJERCICIO 2
class bicicleteria():
    def __init__(self,bicicleta,ganancia,cantidad_de_ventas):
        self.bicicleta = bicicleta
        self.ganancia = ganancia
        self.cantidad_de_ventas = cantidad_de_ventas

    def vender_bicicleta(self):
        print("Usted esta vendiendo una bici")
        cont = 0
        for bicis in self.bicicleta:
            print(f"///---BICI {cont}---///")
            print(f"N° de serie: {bicis.nro_de_serie}\nModelo: {bicis.modelo}\nAño: {bicis.año}\nPrecio: {bicis.precio}\n")
            cont+=1
        serie = input("Ingresar N° de serie de la bicia vender:")
        for bicis in self.bicicleta:
            if bicis.nro_de_serie == serie:
                ganancia = bicis.precio        
                self.bicicleta.remove(bicis)
        self.cantidad_de_ventas += 1
        self.ganancia += ganancia
        return f"Cantidad de ventas: {self.cantidad_de_ventas}\nGanancias: {self.ganancia}"
        

    def comprar_bicicleta(self):
        print("Usted esta comprando una bici")
        nro_de_serie = input("Ingresar N° de serie: ")
        modelo = input("Ingresar Modelo: ")
        año = int(input("Ingresar año: "))
        precio = float(input("Ingresar precio: "))
        bici_nueva = bicicleta(nro_de_serie,modelo,año,precio)
        self.bicicleta.append(bici_nueva)
        return self.bicicleta

class bicicleta():
    def __init__(self,nro_de_serie,modelo,año,precio):
        self.nro_de_serie = nro_de_serie
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def set_precio(self, precio):
        self.precio = precio
    def get_precio(self):
        return f"La Bici cuesta: {self.precio}"
    def get_nro_de_serie(self):
        return f"N° de serie: {self.nro_de_serie}"
        

        

    
       
        
#Declaracion de los objetos de la clase bici para agregar 
#en el atributo de tipo lista de la clase bicicleteria
bici1 = bicicleta("001","Vairo",1995,140000.0)
bici2 = bicicleta("002","Haro",1999,110000.0)
bici3 = bicicleta("003","Shimano",1997,200000.0)
bici4 = bicicleta("004","Montanbike",1990,500000.0)

bicicleteria1 = bicicleteria([bici1,bici2,bici3,bici4],500000.0,7)
print(bicicleteria1.vender_bicicleta())
bicicletas = bicicleteria1.comprar_bicicleta()


bici1.set_precio(10000.0)
print(bici1.get_nro_de_serie())
print(bici1.get_precio())

#Mostramos las bicis disponibles y se muestra que no se 
#encuentra la que se vendio y esta la que se compro, tambien 
#esta la bici1 con el precio cambiado si es que no se la vende
cont = 0
for bicis in bicicletas:
    print(f"///---BICI {cont}---///")
    print(f"N° de serie: {bicis.nro_de_serie}\nModelo: {bicis.modelo}\nAño: {bicis.año}\nPrecio: {bicis.precio}\n")
    cont+=1
