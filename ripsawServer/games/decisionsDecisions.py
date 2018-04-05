#!/usr/bin/python3

"""Decisions... decisions... - conditional statements"""

import random

#LEVEL 1
#Level text
level01text = "Return 1 if the given boolean is True otherwise return 0"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data:
			return 1
		else:
			return 0
		
	data = random.choice([True, False])
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return 0 if the given boolean is False otherwise return 1"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data:
			return 1
		else:
			return 0
		
	data = random.choice([True, False])
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return 1 if the given number is greater than 1024, 0 if the given number is equal to 1024, and -1 if the given number is less than 1024"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data>1024:
			return 1
		elif data == 1024:
			return 0
		else:
			return -1
		
	data = random.randint(1023, 1025)
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return 1 if the given number is greater than 1250 and less than 1750, otherwise return 0"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data>1250 and data <1750:
			return 1
		else:
			return 0
			
	data = random.randint(1000, 2000)
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return 1 if the given number is less than 1250 or greater than 1750, otherwise return 0"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data<1250 or data>1750:
			return 1
		else:
			return 0
		
	data = random.randint(1000, 2000)
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Return 1 if the given number is less than 1250 or greater than 1750, return 0 if the given value is greater than 1400 and less than 1500, otherwise return -1"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data<1250 or data>1750:
			return 1
		elif data>1400 and data<1500:
			return 0
		else:
			return -1
		
	data = random.randint(1000, 2000)
	return [data, solution(data)]

levels = [{"text":level01text, "data":level01data},
	  {"text":level02text, "data":level02data},
	  {"text":level03text, "data":level03data},
	  {"text":level04text, "data":level04data},
	  {"text":level05text, "data":level05data},
	  {"text":level06text, "data":level06data}]