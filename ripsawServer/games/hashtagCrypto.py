#!/usr/bin/python3

"""Hashtag Crypto - hashing and encoding concepts"""

import base64
import codecs
import hashlib
import hmac
import random
import string

#Rand Generator Options
_MAXSTRINGLEN = 20
_MAXHEXSTRLEN = 20
_ALLCHARS = string.ascii_letters+string.digits

def _randString():
	length = random.randrange(1,_MAXSTRINGLEN)
	randStr = ''
	for i in range(abs(length)):
		randStr+=random.choice(_ALLCHARS)
	return randStr

def _randHexStr():
	size = random.randrange(1,_MAXHEXSTRLEN)
	randStr = ''
	for i in range(abs(size)):
		randStr += random.choice(string.hexdigits)
	return randStr

def _randList(size, dataTypeFunc, *args):
	rList = []
	for i in range(abs(size)):
		rList.append(dataTypeFunc(*args))
		
	return rList

#LEVEL 1
#Level text
level01text = "Return the the hex digest (string of hex characters) of the given string using an MD5 hash"

#Level data generator
def level01data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		h = hashlib.md5()
		
		h.update(data.encode('utf-8'))
		return h.hexdigest()
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 2
#Level text
level02text = "Return the the hex digest (string of hex characters) of all the strings in the given list using an SHA-256 hash"

#Level data generator
def level02data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		h = hashlib.sha256()
		for d in data:
			h.update(d.encode('utf-8'))
		return h.hexdigest()
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 3
#Level text
level03text = "Return the Base-64 encoding of the given string"

#Level data generator
def level03data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return base64.b64encode(data.encode('utf-8')).decode('ascii')
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 4
#Level text
level04text = "Return the decoded string of a Base-16 encoded string"

#Level data generator
def level04data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return base64.b16decode(data.encode('utf-8')).decode('ascii')
		
	data = base64.b16encode(_randString().encode('utf-8')).decode('ascii')
	return [data, solution(data)]

#LEVEL 5
#Level text
level05text = "Return the the hex digest (string of hex characters) of the given string using a keyed hash-based message authentication code (HMAC) using a SHA-1 hash and the key 'Ca3saR'"

#Level data generator
def level05data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		key = b"Ca3saR"
		h = hmac.new(key, data.encode('utf-8'), hashlib.sha1)
		return h.hexdigest()
		
	data = _randString()
	return [data, solution(data)]

#LEVEL 6
#Level text
level06text = "Return the given string encoded using ROT13"

#Level data generator
def level06data():
	"""Return data for the level"""
	def solution(data):
		"""Solution to the level - returns answer for generated data"""
		return codecs.encode(data, 'rot_13')
		
	data = _randString()
	return [data, solution(data)]

#List of mappings to access all level text and data in this game
levels = [{"text":level01text, "data":level01data},
	  {"text":level02text, "data":level02data},
	  {"text":level03text, "data":level03data},
	  {"text":level04text, "data":level04data},
	  {"text":level05text, "data":level05data},
	  {"text":level06text, "data":level06data}]
