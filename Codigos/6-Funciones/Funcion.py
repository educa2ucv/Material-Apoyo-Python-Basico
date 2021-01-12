def miFuncion(entrada):
    print("Hola " + entrada)

def suma(a,b):
    return a+b

def foo(a,b,c):
    return a,b,c

def foo2(*args):
    print(args[0],args[1],args[2])


def foo3():
    def interna():
        print("Hola")
    
    interna()

foo3()


