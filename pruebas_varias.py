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

#print(d1)

d2 = (
    dict[('nombre', 'Dulce'), ('edad',25), ('dni', '18469374C')]
)

#print(d2)

#funciones para diccionarios
#print('funcion get', d1.get(100, "No se encontro la clave"))

#if d1.get(100) == None:
#    print("No existe esta busqueda en el diccionario")

#funcion clear, elimina todo el diccionario
#d1.clear()
#print("funcion clear", d1)

#funcion de devolucion de items
valores = d1.items()
#print(valores)

#for k,v in valores:
    #print(str(k)+' - '+ str(v))

#obtener solo las claves
llaves = d1.keys()

#obtener solo los valores
values = d1.values()

#eliminar item especifico
d1.pop(10)

#para cargar nuevos valores a un diccionario
d1.update({'a': 100, 'b': 20})
#print(d1)

#para eliminar de manera aleatoria
d1.popitem()

dic_entero_a_romano = {
    1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
    10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
    100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
    1000: "M", 2000:"MM", 3000:"MMM"}

dic_romano_a_entero = {
    "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

'''
try:
    division = 10/0
except ZeroDivisionError as e:
    print(e)
    print('No se puede dividir ente Cero "0" ')
except Exception as e:
    print(e)
    print('error no reconocido, llame al 457842093')

print("sigue programa")

try:
    prueba = [1,2,3]
    print(prueba[6])
except IndexError as err:
    print(err)
'''
'''
def miException():
    #raise ZeroDivisionError #generar una excepcion
    raise Exception("Esto es mi propia excepcion")

miException()
'''
'''
from main import RomanNumberError

def pruebaExcepcion():
    raise RomanNumberError("Esto es mi excepcion")

pruebaExcepcion()
'''

frutas = ['fresa', 'manzana', 'pera', 'platano']
if 'melon' in frutas:
    print('si existe esta fruta')

if 'pera' not in frutas:
    print('si hay pera')

regla_restas = {'I':('V', 'X'), 'X':('L', 'C'), 'C':('D', 'M')}
print(regla_restas['I'][0])

if 'V' in regla_restas["I"]:
    print("no se encuentra")

valor = ""
if valor:
    print("no esta vacio")
else:
    print("si esta vacio")

print(type("hola"==str))

print(isinstance(5, int))
print(isinstance("valor", str))