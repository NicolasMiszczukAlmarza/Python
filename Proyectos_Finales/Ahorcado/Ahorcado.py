import random

"""
1-El sistema elige una palabra
2-Al usaurio se le van a mostrar los guiones que es la cantidad de letras que va a tener la palabra
3- El jugador elige la letra si acierta le indica donde esta la letra sino pierde una vida
4-Maximo 6 vidas


Metodo choice en una lista de palabra que voy a crear

"""

palabras = ["manzana", "banana", "naranja", "pera", "uva", "fresa", "kiwi", "mango", "cereza", "melon"]
palabra_aleatoria = random.choice(palabras)
palabra_aleatoria=palabra_aleatoria.lower()
lista=list(palabra_aleatoria)
lista2=lista.copy()
lista2 = ['-'] * len(lista2)



vidas=6
while vidas > 0:
    print(f"Tienes {vidas} vidas")
    letra = input("Introduce una letra: ").lower()


    while len(letra) != 1 or not letra.isalpha():
        print("Debes introducir solo UNA letra válida (a-z)")
        letra = input("Introduce una letra: ").lower()

    acierto = False

    for i in range(len(lista)):
        if lista[i]==letra:
            acierto=True
            lista2[i]=letra

    if acierto:
        print(" ".join(lista2))


    if "-" not in lista2:
        print("¡Felicidades! Has adivinado la palabra:", palabra_aleatoria)
        break
    else:
        if not acierto:
            vidas -= 1
            print(f"Has perdido te quedan {vidas} vidas")














