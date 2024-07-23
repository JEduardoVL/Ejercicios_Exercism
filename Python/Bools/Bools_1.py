"""
Este módulo contiene funciones relacionadas con el juego.
"""

def eat_ghost(power_pellet_active, touching_ghost):
    """
    Determina si el jugador puede comer un fantasma.

    Args:
        power_pellet_active (bool): Indica si el pellet de poder está activo.
        touching_ghost (bool): Indica si el jugador está tocando un fantasma.

    Returns:
        bool: True si el jugador puede comer el fantasma, False de lo contrario.
    """
    result = power_pellet_active and touching_ghost
    return result

def score(touching_power_pellet, touching_dot):
    """
    Calcula la puntuación del jugador en función de si está tocando un pellet de poder o una bolita.

    Args:
        touching_power_pellet (bool): Indica si el jugador está tocando un pellet de poder.
        touching_dot (bool): Indica si el jugador está tocando una bolita.

    Returns:
        bool: True si el jugador gana puntos, False de lo contrario.
    """
    result = touching_power_pellet or touching_dot
    return result

def lose(power_pellet_active, touching_ghost):
    """
    Determina si el jugador pierde el juego.

    Args:
        power_pellet_active (bool): Indica si el pellet de poder está activo.
        touching_ghost (bool): Indica si el jugador está tocando un fantasma.

    Returns:
        bool: True si el jugador pierde, False de lo contrario.
    """
    if power_pellet_active and touching_ghost:
        return False
    if not touching_ghost:
        return False
    if not power_pellet_active and touching_ghost:
        return True
    return True

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Determina si el jugador gana el juego.

    Args:
        has_eaten_all_dots (bool): Indica si el jugador ha comido todas las bolitas.
        power_pellet_active (bool): Indica si el pellet de poder está activo.
        touching_ghost (bool): Indica si el jugador está tocando un fantasma.

    Returns:
        bool: True si el jugador gana, False de lo contrario.
    """
    if has_eaten_all_dots and not touching_ghost:
        return True
    if has_eaten_all_dots and touching_ghost and not power_pellet_active:
        return False
    if has_eaten_all_dots and touching_ghost and power_pellet_active:
        return True
    return False
