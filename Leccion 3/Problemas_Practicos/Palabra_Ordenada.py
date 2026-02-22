def ordenar(palabra):
    palabra = palabra.lower()
    return sorted(set(palabra))

print(ordenar("entretenido"))
