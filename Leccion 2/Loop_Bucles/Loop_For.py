lista = ['a','b','c']

for letra in lista:
    num_letra=lista.index(letra)+1
    print(f"Letra {num_letra}: {letra}")

lista2 = ['pablo','laura','fede','luis','julia']
print("")

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)



lista3=[1,2,3,4,5,6]
valor1=0
print("")
for numero in lista3:
    valor1=valor1+numero
    print(valor1)