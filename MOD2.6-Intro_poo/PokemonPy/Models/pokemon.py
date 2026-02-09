import random
# import persistencia


class Movimiento:
    """Clase que representa un movimiento de Pokemon"""
    
    def __init__(self, nombre):
        """
        Constructor de la clase Movimiento
        
        Args:
            nombre (str): Nombre del movimiento
        """
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre


class Pokemon:
    """Clase que representa un Pokemon con sus atributos y métodos de combate"""
    
    def __init__(self, nivel, vida, fuerza, defensa, velocidad):
        """
        Constructor de la clase Pokemon
        
        Args:
            nombre (str): Nombre del Pokemon
            tipo (str): Tipo del Pokemon (Fuego, Agua, Planta, etc.)
            nivel (int): Nivel del Pokemon
            vida (int): Puntos de vida iniciales (100-300)
            fuerza (int): Puntos de ataque (Max 20)
            defensa (int): Puntos de defensa (Max 18)
            velocidad (int): Puntos de velocidad (Max 100)
        """
        # self.nombre = nombre
        self.nivel = nivel
        
        # Validar y asignar vida (100-300)
        if vida < 100:
            self.vida = 100
        elif vida > 300:
            self.vida = 300
        else:
            self.vida = vida
        
        self.vida_maxima = self.vida  # Guardar vida máxima para referencia
        
        # Validar y asignar fuerza (Max 20)
        if fuerza > 20:
            self.fuerza = 20
        else:
            self.fuerza = fuerza
        
        # Validar y asignar defensa (Max 18)
        if defensa > 18:
            self.defensa = 18
        else:
            self.defensa = defensa
        
        # Validar y asignar velocidad (Max 100)
        if velocidad > 100:
            self.velocidad = 100
        else:
            self.velocidad = velocidad
        
        # Lista de movimientos (máximo 4) - Atributo privado
        self.__movimientos = []

    def tipos(self):
        return []
    

    @property
    def movimientos(self):
        """
        Obtiene la lista de movimientos del Pokemon
        
        Returns:
            list: Lista de movimientos (copia para evitar modificación externa)
        """
        return self.__movimientos.copy()

    @movimientos.setter
    def movimientos(self, movimientos):
        """
            - Solo puede tener 4 movimientos
            - Solo puede tener movimientos del mismo tipo del pokemon
            - Sustituir movimiento
        """
        if len(movimientos) != 4:
            raise Exception("La lista de movimientos no tiene 4")

        self.__movimientos = []
        try:
            self.__movimientos = [m for m in movimientos if m.tipo == self.tipo]
        except TypeError: # MovTypeError 
           print("El tipo de movimiento no es correcto")

        if len(self.__movimientos) != 4:
            raise Exception("Deberian haber 4 movimientos algo falla")

    def add_movimiento(self, movimiento, index):
        if movimiento.tipo in self.tipos():
            self.__movimientos[index] = movimiento
        else:
            raise Exception("El tipo de movimiento no es correcto")
        
    
    def ejecutar_movimiento(self, otro_pokemon):
        """
        Ejecuta un movimiento aleatorio contra otro Pokemon
        
        Args:
            otro_pokemon (Pokemon): Pokemon que recibirá el ataque
        
        Returns:
            int: Daño infligido
        """
        if not self.__movimientos:
            print(f"{self.nombre} no tiene movimientos disponibles!")
            return 0
        
        if not self.esta_vivo():
            print(f"{self.nombre} está debilitado y no puede atacar!")
            return 0
        
        # Seleccionar movimiento aleatorio
        movimiento_usado = random.choice(self.__movimientos)
        
        # Calcular daño
        dano = self.fuerza - otro_pokemon.defensa
        
        # El daño mínimo es 1 (para evitar daño 0 o negativo)
        if dano < 1:
            dano = 1
        
        print(f"{self.nombre} usa {movimiento_usado}!")
        
        # Ejecutar el daño en el otro pokemon
        otro_pokemon.recibir_dano(dano)
        
        return dano
    
    def recibir_dano(self, dano):
        """
        Recibe daño y reduce la vida del Pokemon
        
        Args:
            dano (int): Cantidad de daño a recibir
        """
        self.vida -= dano
        
        # La vida no puede ser negativa
        if self.vida < 0:
            self.vida = 0
        
        print(f"{self.nombre} recibe {dano} puntos de daño. Vida restante: {self.vida}/{self.vida_maxima}")
        
        if not self.esta_vivo():
            print(f"{self.nombre} ha sido debilitado!")
    
    def esta_vivo(self):
        """
        Verifica si el Pokemon sigue con vida
        
        Returns:
            bool: True si tiene vida > 0, False en caso contrario
        """
        return self.vida > 0
    
    def __str__(self):
        """
        Representación en string del Pokemon
        
        Returns:
            str: Información del Pokemon
        """
        movimientos_str = ", ".join([str(mov) for mov in self.__movimientos]) if self.__movimientos else "Ninguno"
        estado = "Vivo" if self.esta_vivo() else "Debilitado"
        
        return f"""
            Pokemon: {self.nombre}
            Tipo: {self.tipos()}
            Nivel: {self.nivel}
            Vida: {self.vida}/{self.vida_maxima}
            Fuerza: {self.fuerza}
            Defensa: {self.defensa}
            Velocidad: {self.velocidad}
            Movimientos: {movimientos_str}
            Estado: {estado}
            """


class PokemonVolador(Pokemon):
    def tipos(self):
        return super().tipos() + ["volador"]


class PokemonFuego(Pokemon):
    def tipos(self):
        return super().tipos() + ["fuego"]


class Charizard(PokemonVolador, PokemonFuego):
    def __init__(self, nivel, vida, fuerza, defensa, velocidad):
        self.nombre = "Charizard"
        super().__init__(nivel, vida, fuerza, defensa, velocidad)