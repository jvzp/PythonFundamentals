import unittest
import piglatin

class Test_numbers(unittest.TestCase):
	def test_to_piglatin(self):
		d = piglatin.to_piglatin("happy")
		self.assertEqual(d,"appyhay")
		d = piglatin.to_piglatin("duck")
		self.assertEqual(d,"uckday")
		d = piglatin.to_piglatin("glove")
		self.assertEqual(d,"oveglay")
		d = piglatin.to_piglatin("egg")
		self.assertEqual(d,"eggay")
		d = piglatin.to_piglatin("inbox")
		self.assertEqual(d,"inboxay")
		d = piglatin.to_piglatin("eight")
		self.assertEqual(d,"eightay")

unittest.main()
