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
diccionarios = {1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}

unidades = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
decenas = {10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC"}
centenas = {100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM"}
millares = {1000: "M", 2000:"MM", 3000:"MMM"}

dic_entero_a_romano = {
    1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
    10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
    100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
    1000: "M", 2000:"MM", 3000:"MMM"}


class RomanNumberError(Exception):
    pass

#ingresar 1994 y retornar MCMXCIV
def entero_a_romano(numero): #1994
    numero = str(numero) #transformando en cadena el valor 1994
    numero_list = list(numero) #['1','9','9','4']
    #print(numero_list)
    valor_romano = ''

    cont = 0
    valor_num = 1000
    while cont < 4:
        numero_list[cont] = int(numero_list[cont]) * valor_num
        valor_romano += dic_entero_a_romano.get(numero_list[cont]) #buscar en el diccionario el valor en romano
        cont += 1
        valor_num /= 10

    '''
        for i in range(0, len(numero_list)): #[1000,900,90,4]
            if i == 0:
                numero_list[i] = int(numero_list[i])*1000 #agregar 000 al primer valor
                valor_romano += millares.get(numero_list[i]) #buscar en el diccionario de millares el valor en romano
            elif i == 1:
                numero_list[i] = int(numero_list[i])*100
                valor_romano += centenas.get(numero_list[i])
            elif i == 2:
                numero_list[i] = int(numero_list[i])*10
                valor_romano += decenas.get(numero_list[i])
            elif i == 3:
                numero_list[i] = int(numero_list[i])*1
                valor_romano += unidades.get(numero_list[i])
    '''


    #print(numero_list)

    return valor_romano

print(entero_a_romano(1994))

'''
print(list('1994'))

for i in '1994':
    print(i)

'''