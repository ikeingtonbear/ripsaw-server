#!/usr/bin/python3

"""Second Iteration - Strings and Lists take two"""

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

#Level 1
#Level text
level01text = "Return length of the given string"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		return len(data)
	
	data = _randString()
	return [data, solution(data)]

#Level 2
#Level text
level02text = "Return length of the given list"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		return len(data)
	
	data = _randList(random.randrange(20), random.choice([_randInt,_randString]))
	return [data, solution(data)]

#Level 3
#Level text
level03text = "Return the sum of all the numbers in the list"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		return sum(data)
	
	data = _randList(10, _randInt)
	return [data, solution(data)]

#Level 4
#Level text
level04text = "Return the boolean value of whether 'HelloWorld' is in the given list"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		return "HelloWorld" in data
	
	data = _randList(10, _randString)
	boolVal = random.choice([True, False])
	if boolVal:
		data[random.randrange(len(data))] = "HelloWorld"
	
	return [data, solution(data)]

#Level 5
#Level text
level05text = "Return the boolean value of whether 'HelloWorld' is not in the given list"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		return "HelloWorld" not in data
	
	data = _randList(10, _randString)
	boolVal = random.choice([True, False])
	if boolVal:
		data[random.randrange(len(data))] = "HelloWorld"
	
	return [data, solution(data)]

#Level 6
#Level text
level06text = "Return the given string as a list split on spaces"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		return data.split()
	
	temp = _randList(5, _randString)
	data = " ".join(temp)
	
	return [data, solution(data)]

#Level 7
#Level text
level07text = "Return the given string as a list split on '/'s"

#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		return data.split('/')
	
	temp = _randList(5, _randString)
	data = "/".join(temp)
	
	return [data, solution(data)]

#Level 8
#Level text
level08text = "Return the given list of strings joined together as single string"

#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		return "".join(data)
	
	data = _randList(5, _randString)
	
	return [data, solution(data)]

#Level 9
#Level text
level09text = "Return the given list of strings single string joined by '.'s (periods)"

#Level data generator
def level09data():
	"""Return data for the level"""
	def solution(data):
		return ".".join(data)
	
	data = _randList(5, _randString)
	
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
	  {"text":level09text, "data":level09data}]
