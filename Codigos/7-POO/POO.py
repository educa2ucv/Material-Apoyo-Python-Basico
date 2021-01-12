class Persona:

    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def saludo(self):
        print("Hola a todos")

Persona1 = Persona("Alejandra",21,"Femenino")

Persona1.saludo()
