"""
    Estructuras de Control de Flujo:
        Nos permiten, dada una condición, si esta es cierta ejecutar un
        fragmento de codigo o ejecutar otro fragmento del código.

    Sintaxis Principal:
        *Condicional Simple
            if condicion:
                Bloque de Codigo
        
        *Condicional else
            if condicion 1:
                Bloque de Codigo 1
            else:
                Bloque de Codigo 2

        *Condicional elif
            if condicion 1:
                Bloque de Codigo 1
            elif condicion 2:
                Bloque de Codigo 2
            elif condicion 3:
                Bloque de Codigo 3
"""
"""
    Ejercicio Introductorio: Realice un programa que dada la edad de una persona,
    indique si esta persona es mayor de edad o no.
"""

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
