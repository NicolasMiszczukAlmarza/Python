diccionario={'c1':'valor1','c2':'valor2'}
print(diccionario)

resultado=diccionario['c2']
print(resultado)

cliente={'nombre':'Juan','apellido':'Fuentes','peso':80,'talla':1.76}
consulta=(cliente['apellido'])
print(consulta)

dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])

dic2={'c1':['a','b','c'],'c2':['d','e','f']}

#Imprimir e mayuscula
print(dic2['c2'][1].capitalize())

dic3={1:'a',2:'b'}
print(dic3)
dic3[3]='c'
print(dic3)

print(dic3.keys())
print(dic3.values())