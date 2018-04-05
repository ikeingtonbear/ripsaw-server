#!/usr/bin/python3

"""True B or Not True B - boolean values"""

import random

#LEVEL 1
#Level text
level01text = "Return boolean true"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return True
		
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return boolean false"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return False
		
	data = random.randint(-3000, 3000)
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return the boolean value of whether the given value is less than 1500"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data < 1500
		
	data = random.randint(0, 3000)
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return the boolean value of whether the given value is less than or equal to 1500"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data <= 1500
		
	data = random.randint(0, 3000)
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return the boolean value of whether the given value is greater than 1500"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data > 1500
		
	data = random.randint(0, 3000)
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Return the boolean value of whether the given value is greater than or equal to 1500"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data >= 1500
		
	data = random.randint(0, 3000)
	return [data, solution(data)]

#LEVEL 7
#Level text
level07text = "Return the boolean value of whether the given value is equal to 1500"

#Level data generator
def level07data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data == 1500
		
	data = random.randint(1499, 1501)
	return [data, solution(data)]

#LEVEL 8
#Level text
level08text = "Return the boolean value of whether the given value is less than or equal to 1500"

#Level data generator
def level08data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data != 1500
		
	data = random.randint(1499, 1501)
	return [data, solution(data)]

#LEVEL 9
#Level text
level09text = "Return the boolean value of the given boolean OR-ed with False"

#Level data generator
def level09data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data or False
		
	data = random.choice([True,False])
	return [data, solution(data)]

#LEVEL 10
#Level text
level10text = "Return the boolean value of the given boolean AND-ed with True"

#Level data generator
def level10data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return data and True
		
	data = random.choice([True,False])
	return [data, solution(data)]

#LEVEL 11
#Level text
level11text = "Return the NOT-ed boolean value of the given boolean"

#Level data generator
def level11data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return not data
		
	data = random.choice([True,False])
	return [data, solution(data)]

levels = [{"text":level01text, "data":level01data},
	  {"text":level02text, "data":level02data},
	  {"text":level03text, "data":level03data},
	  {"text":level04text, "data":level04data},
	  {"text":level05text, "data":level05data},
	  {"text":level06text, "data":level06data},
	  {"text":level08text, "data":level07data},
	  {"text":level08text, "data":level08data},
	  {"text":level09text, "data":level09data},
	  {"text":level10text, "data":level10data},
	  {"text":level11text, "data":level11data}]