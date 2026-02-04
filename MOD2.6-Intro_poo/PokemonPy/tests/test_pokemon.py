from models.pokemon import Pokemon, Movimiento



def test_setmovimiento():
    p1 = Pokemon("Sergio", "Bravo", 10000, 100, 20, 500, 99)


    m1 = Movimiento('Pregunta dificil', "Bravo")
    m2 = Movimiento('Pregunta dificil', "Bravo")
    m3 = Movimiento('Pregunta dificil', "Bravo")
    m4 = Movimiento('Pregunta dificil', "Bravo")
    movimientos = [m1,m2,m3,m4]

    p1.movimientos(movimientos)



def test_change_movimiento():
    p1 = Pokemon("Sergio", "Bravo", 10000, 100, 20, 500, 99)
    m1 = Movimiento('Pregunta dificil', "Bravo")
    m2 = Movimiento('Pregunta dificil', "Bravo")
    m3 = Movimiento('Pregunta dificil', "Bravo")
    m4 = Movimiento('Pregunta dificil', "Bravo")
    movimientos = [m1,m2,m3,m4]

    p1.movimientos(movimientos)

    p1.change_movimiento(Movimiento('Contar chiste', "Bravo"), 3)

    assert(len(p1.movimientos) == 4)
    assert(movimientos[3].nombre == "Contar chiste")
    assert(len([x for x in p1.movimientos if x.tipo == p1.tipo]) == 4)