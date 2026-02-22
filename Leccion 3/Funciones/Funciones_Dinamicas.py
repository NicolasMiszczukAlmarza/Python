def chequear_3_cifras(lista):
    lista2=[]
    for n in lista:
        if n in range(100,1000):
            lista2.append(n)

        else:
            pass
    return  lista2

lista=[90,100,200,130,155,67,58,138]
resultado=chequear_3_cifras(lista)
print(resultado)