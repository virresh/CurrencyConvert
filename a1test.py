import unittest
from a1 import *

"""
	Module for testing the a1 module's function's
	Designed for Python 
	Team Information :
	Partner 1						Partner 2
	Name:		Viresh Gupta		Name:		Satvik Jain
	Roll No:	2016116				Roll No:	2016261
"""

class a1test(unittest.TestCase):
	
	def test_exchange(self):
		"""Testing the exchange function"""
		self.assertEqual(exchange("INVALID","INR",5),-1)
		self.assertEqual(exchange("USD","INR",5),333.54735)
	def test_currency_response(self):
		"""Testing the currency_response function"""
		self.assertEqual(currency_response("USD","INR",1.0),'{ "lhs" : "1 United States Dollar", "rhs" : "66.70947 Indian Rupees", "valid" : true, "error" : "" }')


if __name__=='__main__':
	unittest.main()

