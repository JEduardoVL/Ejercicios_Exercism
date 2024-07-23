'''
El problema Collatz Conjecture o 3x-1 se puede resumir de la siguiente manera:

Tome cualquier número entero positivo n. Si n es parejo, divide n por 2 
para obtener n / 2. Si n es impar, multiplicar n por 3 y añadir 1 para 
obtener 3n 1. Repita el proceso indefinidamente. La conjetura establece 
que no importa con qué número empiece, siempre llegarás a 1 eventualmente.

Dado un número n, devuelva el número de pasos necesarios para llegar a 1.
Ejemplos

Comenzando con n = 12, los pasos serían los siguientes:

    12
    6
    3
    10
    5
    16
    8
    4
    2
    1

Resultado en 9 pasos. Así que para la entrada n = 12, el valor de retorno sería 9.
'''

def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    steps_count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        steps_count += 1
    
    return steps_count

print(steps(-10))