palabra='phyton'
lista=[letra for letra in palabra]

print(lista)

lista2=[num if num * 2 > 10 else 'no' for num in range(0,21,2)]
print(lista2)


pies=[10,20,30,40,50]
metro=[p * 3.281 for p in pies]
print(metro)
