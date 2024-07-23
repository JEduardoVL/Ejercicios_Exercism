"""
Este módulo contiene funciones para evaluar la eficiencia del reactor, el equilibrio de la criticidad
y la seguridad del reactor en función de varios parámetros.
"""

def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) * 100
    if efficiency >= 80:
        return 'green'
    if efficiency >= 60:
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    dato = temperature * neutrons_produced_per_second
    if dato < (threshold * 0.9):
        return 'LOW'
    if (threshold * 0.9) <= dato <= (threshold * 1.1):
        return 'NORMAL'
    return 'DANGER'
