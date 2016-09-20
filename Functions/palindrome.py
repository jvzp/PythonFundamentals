import unittest

def palindrome_tester(str_1):

	return True

class Test_numbers(unittest.TestCase):
	def test_prime(self):	
		d = palindrome_tester("ABBA")
		self.assertTrue(d)

unittest.main()





