#!/usr/bin/python3

"""Back to the Abacus - basic math"""

import random

#LEVEL 1
#Level text
level01text = "Return the sum of the given number and 1024"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data + 1024
		
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return the difference of the given number and 1024"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data - 1024
	
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return the product of the given number and 1024"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data * 1024
	
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return the quotient of the given number and 1024"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data / 1024
	
	data = random.randint(-3000, 3000)*1024
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return the remainder of the given number and 1024"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data % 1024
	
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Return the given number negated"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return -data
	
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 7
#Level text
level07text = "Return the absolute value of the given number"

#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return abs(data)
	
	data = data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 8
#Level text
level08text = "Return the the square of the given number"

#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return pow(data, 2)
	
	data = data = random.randint(-3000, 3000)
	return [data, solution(data)]


#List of mappings to access all level text and data in this game
levels = [{"text":level01text, "data":level01data},
	  {"text":level02text, "data":level02data},
	  {"text":level03text, "data":level03data},
	  {"text":level04text, "data":level04data},
	  {"text":level05text, "data":level05data},
	  {"text":level06text, "data":level06data},
	  {"text":level07text, "data":level07data},
	  {"text":level08text, "data":level08data}]