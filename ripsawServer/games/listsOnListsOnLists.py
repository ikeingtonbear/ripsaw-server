#!/usr/bin/python3

"""Lists on lists on lists - lists as you figured out by now"""

import random
import string

_MAXINTSIZE = 1000
_MAXSTRINGLEN = 20

def _randInt():
	return random.randrange(_MAXINTSIZE)

def _randString():
	length = random.randrange(1,_MAXSTRINGLEN)
	randStr = ''
	for i in range(abs(length)):
		randStr+=random.choice(string.ascii_letters)
	return randStr

def _randList(size, dataTypeFunc, *args):
	rList = []
	for i in range(abs(size)):
		rList.append(dataTypeFunc(*args))
		
	return rList

#LEVEL 1
#Level text
level01text = "Return the first item from the given list"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[0]
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return the last item from the given list"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[-1]
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return the 5th item from the given list"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[4]
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return a list containing the first 3 items in the given list"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[:3]
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return a list containing the last 3 items in the given list"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[-3:]
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Return a list containing the items in the indices 3 through the third from the last item (don't include the third from the last item)"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[3:-3]
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 7
#Level text
level07text = "Return a the given list with the 4th item replaced with 'HelloWorld'"

#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		c = data
		c[3] = "HelloWorld"
		return c
		
	data = _randList(10, _randString)
	return [data, solution(data)]

#LEVEL 8
#Level text
level08text = "Return a the given list with 'HelloWorld' inserted at the index 3"

#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.insert(3, 'HelloWorld')
		
	data = _randList(10, _randString)
	return [data, solution(data)]

#LEVEL 9
#Level text
level09text = "Return a the given list with 'HelloWorld' appended to it"

#Level data generator
def level09data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.append('HelloWorld')
		
	data = _randList(10, _randString)
	return [data, solution(data)]

#LEVEL 10
#Level text
level10text = "Return the given list with the item 'HelloWorld' removed"

#Level data generator
def level10data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		data2 = list(data)
		return data2.remove("HelloWorld")
		
	data = _randList(10, _randString)
	data.append("HelloWorld")
	return [data, solution(data)]

#LEVEL 11
#Level text
level11text = "Return the given list in reverse order"

#Level data generator
def level11data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.reverse()
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 12
#Level text
level12text = "Return the given list as a sorted list"

#Level data generator
def level12data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data.sort()
		
	data = _randList(10, random.choice([_randInt, _randString]))
	return [data, solution(data)]

#LEVEL 13
#Level text
level13text = "Given a list (size=2) of lists, return the 1st list extended by the 2nd list"

#Level data generator
def level13data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data[0].extend(data[1])
	
	dataType = random.choice([_randInt, _randString])	
	data = [_randList(5, dataType), _randList(5, dataType)]
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
	  {"text":level13text, "data":level13data}]
