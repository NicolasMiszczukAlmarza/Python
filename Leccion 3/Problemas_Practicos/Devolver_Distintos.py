def devolver_distintos(num1, num2, num3):
    total = num1 + num2 + num3
    lista = [num1, num2, num3]

    if total > 15:
        return max(lista)
    elif total < 10:
        return min(lista)
    else:
        return total - max(lista) - min(lista)

print(devolver_distintos(1, 2, 3))
print(devolver_distintos(6, 5, 5))
print(devolver_distintos(4, 4, 3))
print(devolver_distintos(2, 3, 5))