'''
Un número de Armstrong es un número que es la suma de sus propios 
dígitos cada uno elevado al poder del número de dígitos.

Por ejemplo:

    9 es un número de Armstrong, porque9 = 9^1 = 9
    10 esnoun número de Armstrong, porque10 != 1^2 + 0^2 = 1
    153 es un número de Armstrong, porque:153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    154 esnoun número de Armstrong, porque:154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

Escriba un código para determinar si un número es un número de Armstrong.
'''

def is_armstrong_number(number):
    x = [int(a) for a in str(number)]
    total = 0
    for u in list(x):
        res = u ** len(x) 
        total =total + res
    if total == number:
        return True
    else:
        return False
 