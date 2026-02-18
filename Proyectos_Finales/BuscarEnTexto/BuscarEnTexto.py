""""
Ejercicio Buscar Texto

Paso 1:
Le va a pedir un parrafo al usuario

Paso2:
Luego te va a pedir que introduzcas 3 letras:

Paso3:
Devolver esta infroamcion:
¿Cuantas veces se repite cada letra?
¿Cuantas palabras hay en total?
¿Primera y ultima letra?
¿Texto en orden inverso?
¿Aparece la letra python?

"""

texto=input("Introduce un texto ")
letra1=input("Introduce una letra ")
letra2=input("Introduce una letra ")
letra3=input("Introduce una letra ")

text2=texto.lower()
buscar1=text2.count(letra1)
buscar2=text2.count(letra2)
buscar3=text2.count(letra3)
print(f"La letra {letra1} se encuenta {buscar1} veces")
print(f"La letra {letra2} se encuenta {buscar2} veces")
print(f"La letra {letra3} se encuenta {buscar3} veces")
palabras=len(text2.split())
print(f"Hay {palabras} palabras en el texto")
uno=text2.split()
primera=uno[0]
ultimo=uno[-1]
print(f"La primera palabra es {primera}")
print(f"La ultima palabra es {ultimo}")
inverso=texto.lower().split()
inverso.reverse()
inverso=" ".join(inverso)
print(f"El texto al reves es: ")
print(inverso)
aparece="python" in text2
print(f"¿La letra python aparece?")
print(aparece)
dic={True: "Si", False: "No"}
print(f"¿La palabra python aparece? {dic[aparece]}")