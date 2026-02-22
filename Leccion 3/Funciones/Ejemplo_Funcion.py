precio_cafe=[('capuchino',1.5),('expresso',1.2),('moka',1.9)]
for elemento in precio_cafe:
    print(elemento)

def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
        else:
            pass


    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precio_cafe))
