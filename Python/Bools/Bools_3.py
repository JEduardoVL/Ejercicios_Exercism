'''
Determinar si un triángulo es equilátero, isósceles, o escalane.

Un triángulo equilátero tiene los tres lados de la misma longitud.

Un triángulo isosceles tiene al menos dos lados de la misma longitud. 
(A veces se especifica que tiene exactamente dos lados de la misma 
longitud, pero para los propósitos de este ejercicio diremos al menos dos.)

Un triángulo de escala tiene todos los lados de diferentes longitudes.
'''

def equilateral(sides):
    return all(side > 0 for side in sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return False
    
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]

def scalene(sides):
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return False
        
    return all(side > 0 for side in sides) and len(set(sides)) == 3
