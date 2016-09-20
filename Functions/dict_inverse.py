import unittest

def dict_inverse(d):
	list_1 = d.items()
	d2 = {}
	for k,v in list_1:
		if v in d2:
			d2[v].append(k)
		else:
			d2[v] = [k]
	return d2 

class Test_dict_inverse(unittest.TestCase):
	def test_dict_inverse(self):
		d = { "Oostende" : 8400,
			"Zandvoorde" : 8400,
			"Stene" : 8400,
			"Brugge" : 8000,
			"Gent" : 9000
			}

		d2 = dict_inverse(d)

		self.assertEqual(len(d2), 3)

		self.assertEqual(len(d2[8400]), 3)
		for city in ("Oostende", "Zandvoorde", "Stene"):
			self.assertTrue(city in d2[8400])

		self.assertEqual(d2[8000], ["Brugge"])
		self.assertEqual(d2[9000], ["Gent"])

unittest.main()
