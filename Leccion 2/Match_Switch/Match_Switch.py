# Definimos una función llamada evaluar_estado
# Recibe un parámetro llamado codigo
def evaluar_estado(codigo):

    # Iniciamos la estructura match
    # match compara el valor de "codigo" contra distintos patrones
    match codigo:

        # Si codigo es exactamente 200
        case 200:
            # Retornamos el texto "OK"
            return "OK"

        # Si codigo es exactamente 404
        case 404:
            # Retornamos el texto "No encontrado"
            return "No encontrado"

        # Si codigo es exactamente 500
        case 500:
            # Retornamos el texto "Error interno del servidor"
            return "Error interno del servidor"

        # El guion bajo (_) significa "cualquier otro caso"
        # Es equivalente al "default" en otros lenguajes
        case _:
            # Retornamos este mensaje si no coincidió ningún caso anterior
            return "Código desconocido"


# Llamamos a la función pasando 200 como argumento
# Se ejecutará el case 200
print(evaluar_estado(200))

# Llamamos a la función pasando 404
# Se ejecutará el case 404
print(evaluar_estado(404))

# Llamamos a la función pasando 123
# No coincide con ningún case específico,
# entonces se ejecutará case _
print(evaluar_estado(123))
