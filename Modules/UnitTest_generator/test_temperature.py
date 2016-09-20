import unittest
import temperature

class Test_temperature(unittest.TestCase):
	# Test function for the function celsius_to_kelvin of module temperature
	def test_celsius_to_kelvin(self):

		result = temperature.celsius_to_kelvin(1)
		self.assertAlmostEqual(result, 274.15)



	# Test function for the function kelvin_to_celsius of module temperature
	def test_kelvin_to_celsius(self):

		result = temperature.kelvin_to_celsius(298.15)
		self.assertAlmostEqual(result,25)



unittest.main()
