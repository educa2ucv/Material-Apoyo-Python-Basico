class Persona:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def saludo1(self):
        print("Hola, soy una persona")

class Empleado:
    
    def __init__(self,sueldo):
        self.sueldo = sueldo
    
    def saludo2(self):
        print("Hola, soy un empleado")

class Cajero(Persona,Empleado):

    def __init__(self,nombre,sueldo,nro_caja):

        Persona.__init__(self,nombre)

        Empleado.__init__(self,sueldo)

        self.nro_caja = nro_caja
    
    def saludo3(self):
        print("Hola, soy un cajero")


yo = Cajero("Alexanyer",2500,5)

yo.saludo1()
yo.saludo2()
yo.saludo3()