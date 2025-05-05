import unittest
from Automobilis import Automobilis
from Mikroautobusas import Mikroautobusas
from Klientas import Klientas
from Nuoma import Nuoma

class TestTransportoNuoma(unittest.TestCase):
    def setUp(self):
        self.auto = Automobilis("Toyota", "Corolla", 2020, 50)
        self.mikro = Mikroautobusas("Mercedes", "Sprinter", 2021, 80)
        self.klientas = Klientas("Jonas", "Jonaitis")
        self.nuoma = Nuoma(self.klientas, self.auto, 50)

    def test_automobilis_str(self):
        expected = "Toyota Corolla (2020), Kaina: 50€/d., Būsena: laisva, Durų sk.: 5"
        self.assertEqual(str(self.auto), expected)

    def test_mikroautobusas_tipas(self):
        self.assertEqual(self.mikro.gauti_tipą(), "mikroautobusas")

    def test_klientas_str(self):
        self.assertEqual(str(self.klientas), "Jonas Jonaitis")

    def test_nuoma_pradzia(self):
        self.assertIsNotNone(self.nuoma.pradzia)

if __name__ == '__main__':
    unittest.main()