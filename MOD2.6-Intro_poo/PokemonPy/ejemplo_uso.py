from models.pokemon import Pokemon, Movimiento

# Crear dos Pokemon
pikachu = Pokemon(
    nombre="Pikachu",
    tipo="Eléctrico",
    nivel=25,
    vida=200,
    fuerza=18,
    defensa=12,
    velocidad=90
)

charizard = Pokemon(
    nombre="Charizard",
    tipo="Fuego/Volador",
    nivel=30,
    vida=250,
    fuerza=20,
    defensa=15,
    velocidad=85
)

# Añadir movimientos a Pikachu
pikachu.set_movimiento(Movimiento("Impactrueno"))
pikachu.set_movimiento(Movimiento("Rayo"))
pikachu.set_movimiento(Movimiento("Ataque Rápido"))
pikachu.set_movimiento(Movimiento("Cola Férrea"))

# Añadir movimientos a Charizard
charizard.set_movimiento(Movimiento("Lanzallamas"))
charizard.set_movimiento(Movimiento("Vuelo"))
charizard.set_movimiento(Movimiento("Garra Dragón"))
charizard.set_movimiento(Movimiento("Ascuas"))

# Mostrar información de los Pokemon
print("=" * 50)
print("INFORMACIÓN DE LOS POKEMON")
print("=" * 50)
print(pikachu)
print(charizard)

# Simular un combate
print("=" * 50)
print("¡COMIENZA EL COMBATE!")
print("=" * 50)

# Determinar quién ataca primero (el más rápido)
if pikachu.velocidad >= charizard.velocidad:
    primero = pikachu
    segundo = charizard
else:
    primero = charizard
    segundo = pikachu

print(f"\n{primero.nombre} es más rápido y ataca primero!\n")

# Simular algunos turnos de combate
turno = 1
while pikachu.esta_vivo() and charizard.esta_vivo():
    print(f"\n--- TURNO {turno} ---")
    
    # Ataca el primero
    if primero.esta_vivo():
        primero.ejecutar_movimiento(segundo)
    
    # Si el segundo sigue vivo, contraataca
    if segundo.esta_vivo():
        segundo.ejecutar_movimiento(primero)
    
    turno += 1
    
    # Limitar a 10 turnos para el ejemplo
    if turno > 10:
        print("\n¡El combate ha durado demasiado!")
        break

# Mostrar resultado final
print("\n" + "=" * 50)
print("RESULTADO FINAL")
print("=" * 50)
if pikachu.esta_vivo() and not charizard.esta_vivo():
    print(f"¡{pikachu.nombre} ha ganado el combate!")
elif charizard.esta_vivo() and not pikachu.esta_vivo():
    print(f"¡{charizard.nombre} ha ganado el combate!")
else:
    print("¡El combate terminó en empate!")

print(f"\n{pikachu.nombre} - Vida restante: {pikachu.vida}/{pikachu.vida_maxima}")
print(f"{charizard.nombre} - Vida restante: {charizard.vida}/{charizard.vida_maxima}")
