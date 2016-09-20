import unittest

def armstrong_number(a):

	sum = 0

	temp = a
	while temp > 0:
		digit = temp % 10
		sum += digit ** 3
		temp //= 10

	if a == sum:
		return True
	else:
   		return False

def prime_number(a):

	for x in range(2, a-1, 1):
		if a%x == 0 :
			return False
	return True


class Test_numbers(unittest.TestCase):
	def test_prime(self):	
		d2 = prime_number(1)
		self.assertTrue(d2)
		d2 = prime_number(27)
		self.assertFalse(d2)
		d2 = prime_number(37)
		self.assertTrue(d2)
		d2 = prime_number(23)
		self.assertTrue(d2)
		d2 = prime_number(9)
		self.assertFalse(d2)
		d2 = prime_number(7)
		self.assertTrue(d2)
		d2 = prime_number(4)
		self.assertFalse(d2)

	def test_armstrong(self):
		d = armstrong_number(407)
		self.assertTrue(d)
		d = armstrong_number(664)
		self.assertFalse(d)

unittest.main()
