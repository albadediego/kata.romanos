diccionarios = {"jose":10, "carlos":23, "maria":33}
#print("carlos: ", diccionarios.get("carlos"))

#for i in diccionarios.values():
#for i in diccionarios:
#for c,v in diccionarios.items():
    #print(i)
    #print(diccionarios.get(i))
    #print(c+"-"+str(v))

'''
valor = 3
valor_obtenido = "{:0>4d}".format(valor)
print(valor_obtenido)
print(type(valor_obtenido))
'''

#repaso de diccionario
d1 = {
    "nombre": "Carlos",
    "edad": 45,
    "dni": "B27496583",
    10: "X"
}

print(d1)

d2 = (
    dict[('nombre', 'Dulce'), ('edad',25), ('dni', '18469374C')]
)

print(d2)

#funciones para diccionarios
print('funcion get', d1.get(100, "No se encontro la clave"))

#if d1.get(100) == None:
#    print("No existe esta busqueda en el diccionario")

#funcion clear, elimina todo el diccionario
#d1.clear()
#print("funcion clear", d1)

#funcion de devolucion de items
valores = d1.items()
print(valores)

for k,v in valores:
    print(str(k)+' - '+ str(v))

#obtener solo las claves
llaves = d1.keys()

#obtener solo los valores
values = d1.values()

#eliminar item especifico
d1.pop(10)

#para cargar nuevos valores a un diccionario
d1.update({'a': 100, 'b': 20})
print(d1)

#para eliminar de manera aleatoria
d1.popitem()