#!/usr/bin/python3

from . import hashtagCrypto as testModule
from sys import exit

import base64
import codecs
import hashlib
import hmac

try:
	testLevels = testModule.levels
except:
	print("Unable to load levels from hashtagCrypto")
	exit()

def testLevel1():
	try:
		testLevel = testLevels[0]
	except:
		print("Unable to get testLevel[0]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[0] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		h = hashlib.md5()
		h.update(data)
		solution = h.hexdigest()
	except:
		print("Unable to perform solution")
		return
		
	try:
		if solution == testLevelSolution:
			pass
		else:
			print("Solution Mismatch")
			return
	except:
		print("Unable to to Solve")
		return
	
	print("Test Passed")

def testLevel2():
	try:
		testLevel = testLevels[1]
	except:
		print("Unable to get testLevel[1]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[1] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		h = hashlib.sha256()
		for d in data:
			h.update(d)
		solution = h.hexdigest()
	except:
		print("Unable to perform solution")
		return
		
	try:
		if solution == testLevelSolution:
			pass
		else:
			print("Solution Mismatch")
			return
	except:
		print("Unable to to Solve")
		return
	
	print("Test Passed")

def testLevel3():
	try:
		testLevel = testLevels[2]
	except:
		print("Unable to get testLevel[2]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[2] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = base64.b64encode(data)
	except:
		print("Unable to perform solution")
		return
		
	try:
		if solution == testLevelSolution:
			pass
		else:
			print("Solution Mismatch")
			return
	except:
		print("Unable to to Solve")
		return
	
	print("Test Passed")

def testLevel4():
	try:
		testLevel = testLevels[3]
	except:
		print("Unable to get testLevel[3]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[3] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = base64.b64decode(data)
	except:
		print("Unable to perform solution")
		return
		
	try:
		if solution == testLevelSolution:
			pass
		else:
			print("Solution Mismatch")
			return
	except:
		print("Unable to to Solve")
		return
	
	print("Test Passed")

def testLevel5():
	try:
		testLevel = testLevels[4]
	except:
		print("Unable to get testLevel[4]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[4] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		key = "Ca3saR"
		h = hmac.new(key, data, hashlib.sha1)
		solution = h.hexdigest()
	except:
		print("Unable to perform solution")
		return
		
	try:
		if solution == testLevelSolution:
			pass
		else:
			print("Solution Mismatch")
			return
	except:
		print("Unable to to Solve")
		return
	
	print("Test Passed")

def testLevel6():
	try:
		testLevel = testLevels[5]
	except:
		print("Unable to get testLevel[5]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[5] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = codecs.encode(data, 'rot_13')
	except:
		print("Unable to perform solution")
		return
		
	try:
		if solution == testLevelSolution:
			pass
		else:
			print("Solution Mismatch")
			return
	except:
		print("Unable to to Solve")
		return
	
	print("Test Passed")


tests = [testLevel1,
	      testLevel2,
	      testLevel3,
	      testLevel4,
	      testLevel5,
	      testLevel6]

def run():
	for tl in range(len(testLevels)):
		print("Testing level ",tl+1)
		tests[tl]()
		
if __name__ == "__main__":
	run()