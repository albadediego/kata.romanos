class Persona:
    dni = ""
    direccion = ""
    nacionalidad = ""

    def datos_persona(self):
        print(f"dni: {self.dni}, direccion: {self.direccion}, nacionalidad: {self.nacionalidad}")

class Heroe(Persona): #Heroe hereda los atributos y metodos de la clase Persona, Persona es clase padre de Heroe, Heroe es clase hija de Persona
    #variables o atributos de la clase heroe
    nombre = ""
    poder = ""
    apodo = ""
    edad = 20

    #funcion especial o constructor
    #se ejecuta de manera automatica al crear un objeto de la clase
    def __init__(self, name, power, nickname):
        self.nombre = name
        self.poder = power
        self.apodo = nickname

    def saludar(self):
        print(f"Hola {self.nombre}, tu edad es: {self.edad}")

    def datos(self):
        print(f"Nombre: {self.nombre}, Poder: {self.poder}, Apodo: {self.apodo}, Edad: {self.edad}")

#invocacion de clase
#spiderman es un objeto de la clase heroe, spiderman es una instancia de clase heroe
spiderman = Heroe("Peter Parker", "Super fuerza", "Hombre araña")
spiderman.datos()

ironman = Heroe("Tony Stark", "Millonario", "Hombre de acero")
ironman.edad = 40
ironman.dni = "N53873682"
ironman.direccion = "Malibu california 2454"
ironman.nacionalidad = "EEUU"
ironman.datos()
ironman.datos_persona()

hulk = Heroe("Bruce Banner", "Nervios", "Increible")
hulk.edad = 45
hulk.datos()

print("Pertenece?: ", isinstance(hulk,Heroe))