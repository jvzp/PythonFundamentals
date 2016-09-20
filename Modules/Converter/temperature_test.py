import unittest
import temperature


class Test_numbers(unittest.TestCase):
	def test_celsius_to_kelvin(self):
		d = temperature.celsius_to_kelvin(25)	
		self.assertAlmostEqual(d,298.15)

	def test_kelvin_to_celsius(self):
		d = temperature.kelvin_to_celsius(298.15)
		self.assertAlmostEqual(d,25)

unittest.main()
