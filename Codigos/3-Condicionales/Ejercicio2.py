"""
    Ejercicio 2: En una determinada empresa, sus empleados son evaluados al final de cada año. 
    Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
    traduciéndose en mejores beneficios. 
    Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
    pero no valores intermedios entre las cifras mencionadas. 
    A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
    La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

                Nivel	Puntuación 
                Inaceptable	0.0
                Aceptable	0.4
                Meritorio	0.6 o más
    
    Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
    así como la cantidad de dinero que recibirá el usuario.
"""

puntuacion = float(input("Ingrese su puntuación, por favor: "))

if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
    if puntuacion == 0.0:
        print("Nivel: Inaceptable")
        print("Dinero generado: " + str(0.0*2400))
    elif puntuacion == 0.4:
        print("Nivel: Aceptable")
        print("Dinero generado: " + str(0.4*2400))
    else:
        print("Nivel: Meritorio")
        print("Dinero generado: " + str(puntuacion*2400))
else:
    print("La puntuacion ingresada no es válida")   



















