def primos(*args):
    for num in args:
        if num < 2:
            continue
        cont = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cont += 1
        if cont == 2:
            print(f"El numero {num} es primo")

primos(1,2,3,4,5,6,7,8,9,10,11,12,13)