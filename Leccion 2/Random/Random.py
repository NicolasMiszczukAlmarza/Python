from random import *

#randint()
aleatorio=randint(1,50)
print(aleatorio)

#uniform()
aleatorio=round(uniform(1,5),1)
print(aleatorio)

#random()
aleatorio=random()
print(aleatorio)


#choice()
colores=['azul','rojo','verde','amarillo']
aleatorio=choice(colores)
print(aleatorio)


#shuffle() significa mezcla no se usa con string
numeros=list(range(5,50,5))
shuffle(numeros)
print(numeros)





