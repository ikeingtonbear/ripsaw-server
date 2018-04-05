#!/usr/bin/python3

"""String Theory - understanding strings"""

import random
import string

#Rand Generator Options
_MAXSTRINGLEN = 40
_ALLCHARS = string.ascii_letters+string.digits

def _randChar():
	return random.choice(string.ascii_letters)

def _randString():
	length = random.randrange(10,_MAXSTRINGLEN)
	randStr = ''
	for i in range(abs(length)):
		randStr+=random.choice(_ALLCHARS)
	return randStr

def _randLowerString():
	length = random.randrange(10,_MAXSTRINGLEN)
	randStr = ''
	for i in range(abs(length)):
		randStr+=random.choice(string.ascii_lowercase)
	return randStr

def _randUpperString():
	length = random.randrange(10,_MAXSTRINGLEN)
	randStr = ''
	for i in range(abs(length)):
		randStr+=random.choice(string.ascii_uppercase)
	return randStr

#LEVEL 1
#Level text
level01text = "Return the given string in all upper case letters"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.upper()
		
	data = _randLowerString()
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return the given string in all lower case letters"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.lower()
		
	data = _randLowerString()
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return the given string with the first letter capitalized and all other letters lowercase"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.capitalize()
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return the given string with all the the cases swapped (i.e. AbCde => aBcDE)"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.swapcase()
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return the boolean value of whether all characters in the given string are alphanumeric"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.isalnum()
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Return the string with all the leading and trailing 'A's removed"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.strip('A')
		
	tempData = _randString()
	size = len(tempData)+20
	data = tempData.center(size, "A")
	return [data, solution(data)]

#LEVEL 7
#Level text
level07text = "Return the string with all the 'A's replaced with 'Z's"

#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.replace('A','Z')
		
	tempData = _randString()
	size = len(tempData)+20
	data = tempData.center(size, "A")
	return [data, solution(data)]

#LEVEL 8
#Level text
level08text = "Return 1 if 'StringsRfun' occurs in the given string, otherwise return 0"

#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if "StringsRfun" in data:
			return 1
		else:
			return 0
		
	tempData = _randString()
	if random.choice([True, False]):
		data = tempData.replace(tempData[4], "StringsRfun")
	else:
		data = tempData
	return [data, solution(data)]

#LEVEL 9
#Level text
level09text = "Return the highest index of where 'StringsRfun' occurs in the given string"

#Level data generator
def level09data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.rfind('StringsRfun')
		
	tempData = _randString()
	if random.choice([True, False]):
		data = tempData.replace(tempData[7], "StringsRfun")
	else:
		data = tempData
	return [data, solution(data)]

#LEVEL 10
#Level text
level10text = "Return the letter at index 2 for the given string"

#Level data generator
def level10data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[2]
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 11
#Level text
level11text = "Return the second to last letter for the given string"

#Level data generator
def level11data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[-2]
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 12
#Level text
level12text = "Return a string that starts at the 1st letter and goes to the 10th letter for a given string"

#Level data generator
def level12data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[:10]
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 13
#Level text
level13text = "Return a string that starts at the 8th to last letter and goes to the last letter for a given string"

#Level data generator
def level13data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[-9:]
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 14
#Level text
level14text = "Return a string that starts at the 3rd letter and ends at (includes) the 8th letter for a given string"

#Level data generator
def level14data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[2:9]
		
	data = _randString()
	return [data, solution(data)]


#List of mappings to access all level text and data in this game
levels = [{"text":level01text, "data":level01data},
	  {"text":level02text, "data":level02data},
	  {"text":level03text, "data":level03data},
	  {"text":level04text, "data":level04data},
	  {"text":level05text, "data":level05data},
	  {"text":level06text, "data":level06data},
	  {"text":level07text, "data":level07data},
	  {"text":level08text, "data":level08data},
	  {"text":level09text, "data":level09data},
	  {"text":level10text, "data":level10data},
	  {"text":level11text, "data":level11data},
	  {"text":level12text, "data":level12data},
	  {"text":level13text, "data":level13data},
	  {"text":level14text, "data":level14data}]