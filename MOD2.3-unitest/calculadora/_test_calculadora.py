import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):
    
    def test_suma_dos_numeros(self):
        resultado = suma(2, 3)
        self.assertEqual(resultado, 5)

    def test_resta_dos_numeros(self):
        resultado = resta(2, 3)
        self.assertEqual(resultado, -1)

    def test_division_dos_numeros(self):
        resultado = division(10,2)
        self.assertEqual(resultado, 5)

    def test_multiplicar_dos_numeros(self):
         resultado = multiplicar(2,3)
         pass
    
    def test_porcentaje_15_100(self):
        # calcular 15% de 100
        # si da 15 es que está ok
        pass

    def test_porcentaje_30_10(self):
         # calcular 30% de 10
         # si da 3 es que ok
         pass
    

    def test_suma_dos_numeros_negativos(self):
        # suma dos numeros negativos y deberia dar un 
        # numero negativo equivalente a la suma de los anteriores
        # -5 + -3 = -8
        pass

    # def test_multiplicar_tres_numeros(self):
    #     # multiplicar 5 * 4 * 8 = 160
    #     tup = (5,4,8)
    #     resultado = multiplicar((5,4,8))
    #     pass

    def test_multiplicar_tres_numeros(self):
        # multiplicar 5 * 4 * 8 = 160
        
        resultado = multiplicar(5,4,8)
        # esta multiplicación debería devolver una excepción
        # indicando que no se admiten más de dos numeros por multiplicación

        pass
    


if __name__ == "__main__":
    unittest.main()
