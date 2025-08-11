from romanos_exception import RomanNumberError
from utils.utiles import *

class NumeroRomano:
    def __init__(self, valor):
        self.valor = valor
        self.valor_numerico = 0
        self.valor_romano = ""

        if isinstance(self.valor,str):
           self.valor_romano = self.valor
           self.valor_numerico = self.romano_a_entero(self.valor)
           self.resultado = self.valor_numerico
        elif isinstance(self.valor,int):
           self.valor_numerico = self.valor
           self.valor_romano = self.entero_a_romano(self.valor)
           self.resultado = self.valor_romano
        else:
            raise RomanNumberError("El valor debe ser cadena o entero")

    def entero_a_romano(self, numero:int)->str: 
        if numero > 3999 or numero < 0:
            raise RomanNumberError("El limite esta entre 0 y 3999")
        
        if numero == 0:
            return ""

        numero = "{:0>4d}".format(numero)
        numero_list = list(numero)
        self.valor_romano = ''

        cont = 0
        valor_num = 1000
        while cont < len(numero_list):
            numero_list[cont] = int(numero_list[cont]) * valor_num
            self.valor_romano += dic_entero_a_romano.get(numero_list[cont],'')
            cont += 1
            valor_num /= 10

        return self.valor_romano

    def romano_a_entero(self, romano:str)-> int:
        self.valor_entero = 0
        list_romano = list(romano)
        cont_repes = 0
        caracter_anterior = ""
        caracter_ante_anterior = ""

        for caracter in list_romano:
            if caracter == caracter_anterior:
                if caracter in 'VLD':
                    raise RomanNumberError("Los caracteres 'D', 'L' y 'V' no se pueden repetir.")
                
                cont_repes += 1
                if cont_repes > 2:
                    raise RomanNumberError("No se puede repetir el valor más de tres veces")
            else:
                cont_repes = 0
            
            if caracter_anterior and dic_romano_a_entero.get(caracter_anterior, 0) < dic_romano_a_entero.get(caracter, 0):

                if caracter_anterior in 'VLD':
                    raise RomanNumberError("V, L y D nunca se pueden restar")
                
                if caracter not in regla_restas[caracter_anterior]:
                    raise RomanNumberError(f"{caracter_anterior} solo se puede restar de {regla_restas[caracter_anterior][0]} y {regla_restas[caracter_anterior][1]}")
                
                self.valor_entero -= dic_romano_a_entero.get(caracter_anterior, 0)*2

                if (caracter_anterior == caracter_ante_anterior) and (caracter_anterior in 'IXC'):
                    raise RomanNumberError("I, X y C no se puede restar si hay repeticiones del mismo anteriormente")

            caracter_ante_anterior = caracter_anterior
            caracter_anterior = caracter
            self.valor_entero += dic_romano_a_entero.get(caracter, 0)

        return self.valor_entero 

    #devuelve un string de cualquier parametro de una clase
    def __repr__(self):
        return str(self.resultado)
    
    def num_romano_entero(self):
        return self.resultado
    
    def __add__ (self, obj):
        if isinstance(obj, NumeroRomano):
            return NumeroRomano(self.valor_numerico + obj.valor_numerico)

'''
prueba1 = NumeroRomano("XXVII")
print("Romano a entero: ", prueba1)
print("Valor numerico: ", prueba1.valor_numerico)
print("Valor romano: ", prueba1.valor_romano)
print("------------------------------------")
prueba2 = NumeroRomano(34)
print("Entero a romano: ", prueba2)
print("Valor numerico: ", prueba2.valor_numerico)
print("Valor romano: ", prueba2.valor_romano)
'''