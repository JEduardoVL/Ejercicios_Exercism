'''
Se produce un año bisaúd (en el calendario gregoriano):

    En cada año que es uniformemente divisible a 4.
    A menos que el año sea uniformemente divisible por 100, 
    en cuyo caso es sólo un año bisata si el año también es uniformemente 
    divisible en 400.

Algunos ejemplos:

    1997 no fue un año bisata, ya que no es divisible por 4.
    1900 no fue un año bisata, ya que no es divisible por 400.
    2000 fue un año bisata.

'''
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False