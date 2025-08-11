from romano_class import NumeroRomano

continuar = True

while continuar:
    print("Inicio del programa")
    opcion = input("¿Que desea realizar? \nRomano_a_entero: presione 'r' \nEntero_a_romano: presione 'e'")

    print("Ejecucion del programa")
    if opcion == "r":
        try:
            valor = input("Ingrese el valor en romano: ")
            obj1 = NumeroRomano(valor)
            print(f"El valor de {obj1.valor} es igual a {obj1.valor_entero}")
        except NumeroRomano as e:
            print(e)
        except Exception as e:
            print("Error python: ", e)
    elif opcion == "e":
        try:
            valor = int(input("Ingrese el valor en entero: "))
            obj2 = NumeroRomano(valor)
            print(f"El valor de {obj2.valor} es igual a {obj2.valor_romano}")
        except NumeroRomano as e:
            print(e)
        except Exception as e:
            print("Error python: ", e)

    seguir = input("Si desea salir del programa presione 'n': ")
    if seguir == "n":
        continuar = False
        print("Fin del programa")