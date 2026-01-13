import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):
    def test_suma_dos_numeros(self):
            resultado = suma(2, 3)
            self.assertEqual(resultado, 5)

if __name__ == "__main__":
    unittest.main()
