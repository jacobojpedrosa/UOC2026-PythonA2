# Escenario
# Definir que pokemons van a combatir (2 -> p1 y p2)
# Definir quien inicia el ataque: el que tenga más velocidad
# El tipo del movimiento tiene que ser del mismo que el tipo del pokemon
# Logica de turno: 
# - 1 accion por turno para cada pokemon
# - ataca 1 pokemon el 2 recibe daño en función del p1.ataque - p2.defensa
# - ataca 2 pokemon el 1 recibe daño en función del p2.ataque - p1.defensa

# condiciones victoria o derrota
# El primer pokemon que se queda a vida <= 0 pierde 
 
from models.pokemon import Pokemon, Movimiento

def test_crearpokemon():
    # validar que se crear el pokemon correctamentee
    pass


def test_ataque():
    pass

def test_tipomovimiento():
    pass