''' Module a1 for HW 1
	This module has functions for fetching the currency data
	designed for python 2.7

	Team Information :
	Partner 1						Partner 2
	Name:		Viresh Gupta		Name:		Saatvik Jain
	Roll No:	2016116				Roll No:	2016261
'''
import urllib

''' Global Variables '''
err=''
''' ---------------- '''

def currency_response(from_c,to_c,amount_from):
	'''	Return Value : This function returns returns a JSON string
		obtained from the source server
		
		Parameters:		Preconditions:
		from_c			string for a currency code which is in hand
		to_c			string for a currency code to convert to
		amount_from		float value representing the amount to convert
	'''
	query_string = "http://cs1110.cs.cornell.edu/2015fa/a1server.php?from=" + from_c +"&to=" + to_c + "&amt=" + str(amount_from)
	web_page = urllib.urlopen(query_string)		#contains the web page returns
	string = str(web_page.read())			#contains the JSON string
	return string

def has_error(json_string):
	'''	This functions return's True/False depending on whether the
		retrieved JSON string has an error or not.
		Parameter:					Precondition:
		json -	String to process	It is the responce to a currency query
	'''
	
	if(json_string[json_string.find("valid")+9:(json_string.find("valid")+14)]=="false"):
		global err 
		err = json_string[json_string.find("error")+10:json_string.find("}")-2]	#sets the specification of what error occurred
		return True
	else:
		return False				#no error

def before_space(s):
	'''	This function returns a substring upto but not including the
		first space in string s.

		Parameter:					Precondition:
		s - string to slice			Must have atleast one space
	'''
	x = s[:s.find(' ')]
	return x

def after_space(s):
	'''	This function returns a substring that includes everything after
		the first space.
		Parameter:					Precondition:
		s - string to slice			Must have atleast one space
	'''
	x = s[s.find(' '):]
	return x

def exchange(from_c,to_c,amount_from):
	'''	Return Value : This function returns value amount_from 
		in currency from to the corresponding value in currency to.
		or return -1 if input values are invalid
		
		Parameters:		Preconditions:
		from_c			string for a currency code which is in hand
		to_c			string for a currency code to convert to
		amount_from		float value representing the amount to convert

		Usage :
		exchange("USD","INR",1.0)
	'''
	data = currency_response(from_c,to_c,amount_from)

	if(has_error(data)):
		return -1
	else:
		
		converted_value = float(before_space(data[data.find("rhs")+8:]))
		return converted_value

if(__name__ == '__main__'):
	fromCode = raw_input("Enter From Country Code :\t")
	toCode = raw_input("Enter To Country Code :\t\t")

	#invalid amount error handling code
	try:
		amt = float(raw_input("Enter the amount to convert:\t"))
	except ValueError:
		print("Wrong Amount Entered.\n")
		exit(0)

	val = exchange(fromCode,toCode,amt)

	if(val != -1):
		print (val)
	else:
		print ("Error Encountered : \t"+err)
