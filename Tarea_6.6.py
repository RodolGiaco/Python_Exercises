
def separar(lista):
    par = []
    impar = []
    for dato in lista:
        if dato%2 == 0:
            par.append(dato)
        else:
            impar.append(dato)

    par.sort()
    impar.sort()
    return par, impar


lista = [7,1,5,8,7,3,6,4,5,1,8]
par, impar = separar(lista)
print(par)
print(impar)
