from random import *
nombre=input("Introduce tu nombre ")
print(f"Hola {nombre} tienes 8 intentos para adivinar el numero secreto entre el 1 y el 100 ")
num=0
numsec=randint(1,101)

vida=8

while vida > 0:
    print(f"Tienes {vida} vidas ")
    num=int(input("Introduce un numero "))
    if num < 1 or num > 100:
        print(f"El numero que has introducido esta fuera del rango ")
        vida-=1

    elif numsec > num:
        print(f"El numero secreto es mayor ")
        vida -= 1

    elif numsec < num:
        print(f"El numero secreto es menor ")
        vida -= 1

    elif num == numsec:
        print(f"Enhorabuena has acertado con {vida} vidas ahora intenta acertar otro nuevo numero secreto ")
        vida=8
        numsec = randint(1, 101)


    if vida == 0:
        print(f"Has agotado todas las vidas, más suerte la proxima vez ")
        print(f"El numero secreto era {numsec}")




