import unittest
import temperature


class Test_numbers(unittest.TestCase):
	def test_celsius_to_kelvin(self): 	
		self.assertAlmostEqual(temperature.celsius_to_kelvin(25),298.15)
		self.assertRaises(AssertionError, temperature.celsius_to_kelvin, -274)

	def test_kelvin_to_celsius(self):
		self.assertAlmostEqual(temperature.kelvin_to_celsius(298.15),25)
		self.assertRaises(AssertionError, temperature.kelvin_to_celsius, -1)

unittest.main()
