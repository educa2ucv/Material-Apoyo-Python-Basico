"""
    Ejercicio 1: Escribir un programa que almacene la cadena de caracteres
    "contraseña" en una variable, pregunte al usuario por la contraseña hasta que
    introduzca la contraseña correcta.
"""

password = 'alexanyernas'

password_user = input("Ingrese la contraseña: ")

while password != password_user:
    print("La contraseña ingresada es INCORRECTA")
    password_user = input("Ingrese nuevamente la contraseña: ")

print("La contraseña ingresada es CORRECTA")
