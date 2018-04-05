#!/usr/bin/python3

from . import merriamWebstersUrban as testModule
from sys import exit

try:
	testLevels = testModule.levels
except:
	print("Unable to load levels from merriamWebstersUrban")
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
		solution = len(data)
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
		solution = data.keys()
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
		solution = data.values()
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
		solution = "HelloWorld" in data
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
		solution = data["HelloWorld"]
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
		solution = data
		solution["Hello"] = "World"
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

def testLevel7():
	try:
		testLevel = testLevels[6]
	except:
		print("Unable to get testLevel[6]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[6] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data[0]
		solution.update(data[1])
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

def testLevel8():
	try:
		testLevel = testLevels[7]
	except:
		print("Unable to get testLevel[7]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[7] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data
		for k,v in data.iteritems():
			solution[k] = v+20
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

def testLevel9():
	try:
		testLevel = testLevels[8]
	except:
		print("Unable to get testLevel[8]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[8] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data
		for k,v in data.iteritems():
			solution[k] = "HelloWorld"
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
	      testLevel6,
	      testLevel7,
	      testLevel8,
	      testLevel9]

def run():
	for tl in range(len(testLevels)):
		print("Testing level ",tl+1)
		tests[tl]()
		
if __name__ == "__main__":
	run()