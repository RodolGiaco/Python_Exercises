def relacion(n1,n2):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    elif n1 == n2:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))
