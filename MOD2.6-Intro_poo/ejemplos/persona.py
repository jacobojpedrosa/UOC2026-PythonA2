class Persona:
    _nombre = None
    _edad = None


    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def saludar(self):
        return f"Hola, me llamo {self._nombre} mi edad es {self._edad}"