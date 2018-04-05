#!/usr/bin/python3

"""Just a bit loopy - looping techniques"""

import random, string

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
level01text = "Given a number, sum the range of numbers up to, but not including the given number"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		total = 0
		for i in range(data):
			total+=i
		return total
	
	data = _randInt()
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Given a list (size 2, [lowerbound, upperbound]) of numbers, sum the range of numbers up to, but not including the upper bound number"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		total = 0
		for i in range(data[0], data[1]):
			total+=i
		return total
	
	tempData = _randInt()
	data = [tempData, tempData+_randInt()]
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Given a list (size 2, [lowerbound, upperbound]) of numbers, if the first number is even, sum all the even numbers in the given range, or if the first number is odd, sum all the odd numbers in the given range, do not include the upper bound"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		total = 0
		for i in range(data[0], data[1],2):
			total+=i
		return total
	
	tempData = _randInt()
	data = [tempData, tempData+_randInt()]
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Given a list of strings, return the same list with all strings capitalized"
#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		caps = []
		for s in data:
			caps.append(s.upper())
		return caps
	
	data = _randList(10, _randString)
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Given a list of integers, return the same list with all numbers increased by 20"
#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		ans = []
		for i in data:
			ans.append(i+20)
		return ans
	
	data = _randList(10, _randInt)
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Given a list of tuples (list of size 2), return a list of integers where the first number in the tuple is subtracted from the second in the tuple"
#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		ans = []
		for i, j in data:
			ans.append(j-i)
		return ans
	
	data = _randList(10, _randList, 2, _randInt)
	return [data, solution(data)]

#LEVEL 7
#Level text
level07text = "Given a list of tuples (list of size 2), return a list of strings where the first in the tuple is appended the second in the tuple"
#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		ans = []
		for i, j in data:
			ans.append("".join([j,i]))
		return ans
	
	data = _randList(10, _randList, 2, _randString)
	return [data, solution(data)]

#LEVEL 8
#Level text
level08text = "Given a list of lists of strings, return a single list with all the strings in lowercase"
#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		ans = []
		for i in data:
			for j in i:
				ans.append(j.lower())
		return ans
	
	data = _randList(5, _randList, 3, _randString)
	return [data, solution(data)]

#LEVEL 9
#Level text
level09text = "Given a list of lists of integers, begin with the last integer, and subtract the one before it, then subtract the next one before that until you get to the first integer"
#Level data generator
def level09data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to Level - returns answer for generated data"""
		data2 = data[:-1]
		diff = data[-1]
		for i in reversed(data2):
			diff-=i
		return diff
	
	data = _randList(10, _randInt)
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
