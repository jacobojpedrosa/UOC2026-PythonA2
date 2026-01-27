from persona import Persona

alumnos = []

alumnos.append(Persona("Ruben", 24))
alumnos.append(Persona("Noemí", 22))
alumnos.append(Persona("Edisson", 52))
alumnos.append(Persona("Juan José", 34))

for i in alumnos:
    print(i.saludar())




