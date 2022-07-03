def recortar(nr, li,ls):
    if nr < li:
        return li
    elif nr > ls:
        return ls
    elif  li < nr < ls:
        return nr


print(recortar(15,0,10))
