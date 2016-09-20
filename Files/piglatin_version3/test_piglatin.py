import unittest
import piglatin

class Test_numbers(unittest.TestCase):
	def test_to_piglatin(self):
		d = piglatin.to_piglatin("happy")
		self.assertEqual(d,"appy-hay")
		d = piglatin.to_piglatin("duck")
		self.assertEqual(d,"uck-day")
		d = piglatin.to_piglatin("glove")
		self.assertEqual(d,"ove-glay")
		d = piglatin.to_piglatin("egg")
		self.assertEqual(d,"egg-ay")
		d = piglatin.to_piglatin("inbox")
		self.assertEqual(d,"inbox-ay")
		d = piglatin.to_piglatin("eight")
		self.assertEqual(d,"eight-ay")

	def test_from_piglatin(self):
		d = piglatin.from_piglatin("appy-hay")
		self.assertEqual(d,"happy")
		d = piglatin.from_piglatin("egg-ay")
		self.assertEqual(d,"egg")

unittest.main()
