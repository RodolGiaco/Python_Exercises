class persona():
    def __init__(self,nombre,edad,DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_DNI(self):
        return self.__DNI


    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self, edad):
        self.__edad = edad
    def set_DNI(self, DNI):
        self.__DNI = DNI

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.DNI}\n")
    def esMayorDeEdad(self):
        if self.edad > 18:
            return True
        else:
            return False


class cuenta(persona):
    def __init__(self,titular,cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular
    def get_cantidad(self):
        return self.__cantidad
  

    def set_titular(self, titular):
        self.__titular = titular
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular}\nCantidad: {self.__cantidad}")
    def ingresar(self,cantidad):
        if self.__cantidad > 0:
            self.__cantidad += cantidad
        else:
            return
    def retirar(self,cantidad):
            self.__cantidad -= cantidad
        
 



persona1 = persona("Rodol",25,41083266)
# persona1.mostrar()
# print(persona1.esMayorDeEdad())

cuenta1 = persona.cuenta(persona1, 20000)
print(cuenta1.mostrar())
# cuenta1 = cuenta("Rodo",1000)
# cuenta1.mostrar()
# cuenta1.ingresar(200)
# cuenta1.mostrar()
# cuenta1.retirar(200)
# cuenta1.mostrar()
