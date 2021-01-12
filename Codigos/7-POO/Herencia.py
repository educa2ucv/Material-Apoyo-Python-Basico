class Persona:

    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def saludo(self):
        print("Hola a todos")

class Empleado(Persona):

    def __init__(self,nombre,edad,genero,sueldo,puesto):

        Persona.__init__(self,nombre,edad,genero)

        self.sueldo = sueldo
        self.puesto = puesto

    def obtenerSueldo(self):
        print("Mi sueldo es de: " + str(self.sueldo))

Yo = Empleado("Alexanyer",21,"Masculino",2500.00,"Cajero")

Yo.obtenerSueldo()