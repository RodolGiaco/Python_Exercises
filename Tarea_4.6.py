lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = lista_1 + lista_2  
lista_nueva = []
lista_nueva = list(set(lista_3)) 
print(lista_nueva)

lista_aux = lista_1 + lista_2
#La otra manera que inteprete es que no se repita la 
#palabra me salio mas o menos
for i in range(len(lista_3)):
    for j in range(i +1,len(lista_3)):
        if lista_3[i] == lista_3[j]:
              lista_aux[j:j+1] = []
else:
    print(lista_aux)


    
