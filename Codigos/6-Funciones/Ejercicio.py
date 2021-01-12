"""
    Ejercicio 1: Escribir una función que reciba una muestra
    de números en una lista y devuelva otra lista con sus cuadrados.

    Ejemplo: listaA = [2,3,4,5]
             resultado = [4,9,16,25]
"""

def cuadrados(lista):
    resultado = []
    for i in lista:
        resultado.append(i**2)
    return resultado

numeros = [2,3,4,5]
resultado = cuadrados(numeros)
print(resultado)
