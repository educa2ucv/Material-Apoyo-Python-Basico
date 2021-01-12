"""
    Ejercicio 2: Escribir un programa en el que se pregunte al usuario por una frase
    y una letra, y muestre por pantalla el número de veces que aparece
    la letra en la frase.
"""

frase = input("Ingrese una frase, por favor: ")
letra = input("Ingrese una letra a contar: ")
cont = 0

for elemento in frase:
    if elemento == letra:
        cont = cont + 1

print("La cantidad de veces que aparece la letra " + letra + " es: " + str(cont))
