#!/usr/bin/python3

"""Merriam Webster's Urban - Dictionaries"""

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

def _randDict(size, keyTypeFunc, valTypeFunc, *args):
	rDict = {}
	for i in range(abs(size)):
		rDict[keyTypeFunc()] = valTypeFunc(*args)
	return rDict


#LEVEL 1
#Level text
level01text = "Return the len of the dictionary"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return len(data)
		
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return a sorted list of the dictionary's keys"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return list(data.keys()).sort()
	
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return the a sorted list of the dictionary's values"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return list(data.values()).sort()
	
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return the boolean of whether the key 'HelloWorld' is in the dictionary"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return 'HelloWorld' in data
		
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
	if random.choice([True,False]):
		data["HelloWorld"] = _randString()
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return the the value of the key 'HelloWorld"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data['HelloWorld']
	
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
	data["HelloWorld"] = _randString()
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Insert the value 'World' with the key of 'Hello' into the given dictionary"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		data2 = data
		data2['Hello'] = 'World'
		return data2
	
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
	return [data, solution(data)]

#LEVEL 7
#Level text
level07text = "Given a list (size 2) of dictionaries, update the first dictionary with the second"

#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		a,b = data
		return a.update(b)
	
	data1 = _randDict(random.choice(range(1,8)), _randString, _randString)
	data2 = _randDict(random.choice(range(1,8)), _randString, _randString)
	data =[data1, data2]
	return [data, solution(data)]

#LEVEL 8
#Level text
level08text = "Given a dictionary with strings as keys, and integers as values, increase all values by 20"

#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		tempData = data
		for k,v in tempData.items():
			tempData[k] = v+20
		return tempData
	
	data = _randDict(random.choice(range(1,20)), _randString, _randInt)
	return [data, solution(data)]

#LEVEL 9
#Level text
level09text = "Given a dictionary with strings as keys, and strings as values, replace all the values with 'HelloWorld'"

#Level data generator
def level09data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		tempData = data
		for k,v in tempData.items():
			tempData[k] = 'HelloWorld'	
		return tempData
	
	data = _randDict(random.choice(range(1,20)), _randString, _randString)
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
