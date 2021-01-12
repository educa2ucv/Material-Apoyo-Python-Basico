"""
    Ejercicio 2: Escribir una función que reciba una muestra de números
    en una lista y devuelva un diccionario con su suma y multiplicación.
"""

def suma(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    return resultado

def multiplicacion(lista):
    resultado = 1
    for i in lista:
        resultado = resultado * i
    return resultado

def principal(numeros):
    diccionario = {}
    diccionario["suma"] = suma(numeros)
    diccionario["multiplicacion"] = multiplicacion(numeros)
    return diccionario

numeros = [1,2,3,4,5,6,7,8,9]
print(principal(numeros))
