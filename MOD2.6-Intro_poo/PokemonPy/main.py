# Script que me va a ejecutar la logica siguiente:

# Escenario
# Definir que pokemons van a combatir (2 -> p1 y p2)
# Definir quien inicia el ataque: el que tenga más velocidad
# Logica de turno: 
# - 1 accion por turno para cada pokemon
# - ataca 1 pokemon el 2 recibe daño en función del p1.ataque - p2.defensa
# - ataca 2 pokemon el 1 recibe daño en función del p2.ataque - p1.defensa

# condiciones victoria o derrota
# El primer pokemon que se queda a vvida <= 0 pierde
from models.pokemon import Movimiento, Pikachu

# p1 = Pokemon("Sergio", "Bravo", 10000, 100, 20, 500, 99)


# m1 = Movimiento('Pregunta dificil', "Bravo")
# m2 = Movimiento('Pregunta dificil', "Bravo")
# m3 = Movimiento('Pregunta dificil', "Bravo")
# m4 = Movimiento('Pregunta dificil', "Bravo")
# movimientos = [m1,m2,m3,m4]

# p1.movimientos(movimientos)


pika = Pikachu(100, 100, 100, 100, 100)
print(pika)