'''
Calcular el número de granos de trigo en un tablero de ajedrez dado que el 
número en cada cuadrado se duplica.

Una vez hubo un sabio siervo que salvó la vida de un príncipe. 
El rey prometió pagar lo que el sirviente pudiera soñar. S
abiendo que el rey amaba ajedrez, el siervo le dijo al rey que le gustaría 
tener granos de trigo. Un grano en el primer cuadrado de una tabla de ajedrez, 
con el número de granos duplicándose en cada cuadrado sucesivo.

Hay 64 cuadrados en una tabla de ajedrez (donde el cuadrado 1 tiene un grano, 
cuadrado 2 tiene dos granos, y así es).

Escriba código que muestre:

    cuántos granos estaban en un cuadrado dado, y
    el número total de granos en el tablero de ajedrez

'''

def square(number):
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    
    grains = 1 << (number - 1)  
    return grains

square(4)

def total():
    total_grains = (1 << 64) - 1  
    return total_grains

total()