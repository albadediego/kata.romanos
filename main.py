'''
1- Crear una funcion que pase de entero > 0 y < 4000 a romano
2- Cualquier otra entrada dar error
3- Límite 3999

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor a cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero o positivo")
f) 4.5 -> RomanNumberError("Debe ser un numero entero")

M ---> 1000
D ----> 500
C ----> 100
L ----> 50
X --->10
V ---> 5
I ---> 1
'''

dic_entero_a_romano = {
    1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
    10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
    100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
    1000: "M", 2000:"MM", 3000:"MMM"}

dic_romano_a_entero = {
    "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

regla_restas = {'I':('V', 'X'), 'X':('L', 'C'), 'C':('D', 'M')}

class RomanNumberError(Exception):
    pass

def romano_a_entero(romano:str)-> int:
    valor_entero = 0
    list_romano = list(romano)
    cont_repes = 0
    caracter_anterior = ""

    if 'DD' in romano or 'LL' in romano or 'VV' in romano:
        raise RomanNumberError("Los caracteres 'D', 'L' y 'V' no se pueden repetir.")

    for caracter in list_romano:
        if caracter == caracter_anterior:
            #if caracter == 'V' or caracter == 'L' or caracter == 'D':
            #    raise RomanNumberError("Los caracteres 'D', 'L' y 'V' no se pueden repetir.")
            
            cont_repes += 1
            if cont_repes > 2:
                raise RomanNumberError("No se puede repetir el valor más de tres veces")
        else:
            cont_repes = 0
        
        if dic_romano_a_entero.get(caracter_anterior, 0) < dic_romano_a_entero.get(caracter, 0):

            if caracter_anterior and caracter_anterior in 'VLD':
                raise RomanNumberError("V, L y D nunca se pueden restar")
            
            if caracter_anterior and caracter not in regla_restas[caracter_anterior]:
                raise RomanNumberError(f"{caracter_anterior} solo se puede restar de {regla_restas[caracter_anterior][0]} y {regla_restas[caracter_anterior][1]}")
            
            valor_entero -= dic_romano_a_entero.get(caracter_anterior, 0)*2

        caracter_anterior = caracter
        valor_entero += dic_romano_a_entero.get(caracter, 0)

    return valor_entero 

#print(romano_a_entero('LL'))
#'D', 'L' y 'V' no se pueden repetir.

def entero_a_romano(numero:int)->str: 
    numero = "{:0>4d}".format(numero) #transforma el numero dado a un str de 4 digitos y si es menos lo completa con ceros a la izquierda
    numero_list = list(numero) #transformando el str dado en una lista de string por cada caracter
    valor_romano = ''

    cont = 0
    valor_num = 1000
    while cont < len(numero_list):
        numero_list[cont] = int(numero_list[cont]) * valor_num
        valor_romano += dic_entero_a_romano.get(numero_list[cont],'')
        cont += 1
        valor_num /= 10

    return valor_romano

#print(entero_a_romano(1994))
#print(entero_a_romano(333))

