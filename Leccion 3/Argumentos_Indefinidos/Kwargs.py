def suma(num1,num2,*args,**kwargs):
    print(f"El primer valor es: {num1}")

    print(f"El primer valor es: {num2}")

    for item in args:
        print(f"arg = {item}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


suma(1,2,1,2,3,4,5,x='uno',y='dos',z='tres')