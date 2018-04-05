#!/usr/bin/python3

"""Bits and Pieces - understanding bitwise operations"""

import random
import string

#LEVEL 1
#Level text
level1text = "Return 1 if the given boolean is True otherwise return 0"

#Level data generator
def level1data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		if data:
			return 1
		else:
			return 0
		
	data = random.choice([True, False])
	return [data, solution(data)]

#List of mappings to access all level text and data in this game
levels = [{"text":level1text, "data":level1data}]