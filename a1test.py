import unittest
from a1 import *

"""
	Module for testing the a1 module's function's
	Designed for Python 
	Team Information :
	Partner 1						Partner 2
	Name:		Viresh Gupta		Name:		Saatvik Jain
	Roll No:	2016118				Roll No:	2016261
"""

class a1test(unittest.TestCase):
	
	def test_exchange(self):
		"""Testing the exchange function"""
		self.assertEqual(exchange("INVALID","LKR",5),-1)
		self.assertEqual(exchange("USD","INR",5),333.54735)
		self.assertEqual(exchange("LTL","ZWL",13),1377.2797844181)
		self.assertEqual(exchange("JPY","INR",5000000),3211428.8492682)
		self.assertEqual(exchange("GBP","AED",-5),-1)
		self.assertEqual(exchange("GBP","AED","5"),24.416381934935)

	def test_currency_response(self):
		"""Testing the currency_response function"""
		self.assertEqual(currency_response("USD","INR",1.0),'{ "lhs" : "1 United States Dollar", "rhs" : "66.70947 Indian Rupees", "valid" : true, "error" : "" }')

	def test_hasError(self):
		"""Testing the has_error() function"""
		self.assertEqual(has_error('{ "lhs" : "1 United States Dollar", "rhs" : "66.70947 Indian Rupees", "valid" : true, "error" : "" }'),False)


if __name__=='__main__':
	unittest.main()

