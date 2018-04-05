#!/usr/bin/python3

"""RIPSAW Demo game"""

#LEVEL 1
#Level 1 text
level01text = "Echo back the data"

#Level 1 data generator
def level01data():
	"""Return data for Level 1"""
	def solution(data):
		"""Solution to Level 1 - returns answer for generated data"""
		return data
	
	testData = "hello"
	return [testData, solution(testData)]

#List of mappings to access all level text and data in this game
levels = [{"text":level01text, "data":level01data}]