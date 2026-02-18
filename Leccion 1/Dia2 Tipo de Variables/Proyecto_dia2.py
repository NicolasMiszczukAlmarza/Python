#preguntar nombre y cuanto han vendido este mes
# respodner frase: ok nombre. este mes ganaste xeuros

nombre=input("¿cual es tu nombre? ")
ganancias=input("¿cuanto has ganado este mes? ")
decimales=float(ganancias)
comision=decimales*0.13
comision2=round(comision,2)
respuesta=f"Ok {nombre}, este mes ganaste {comision2} euros"
print(respuesta)
