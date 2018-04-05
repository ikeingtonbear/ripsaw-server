#!/usr/bin/python3

from . import justABitLoopy as testModule
from sys import exit

try:
	testLevels = testModule.levels
except:
	print("Unable to load levels from justAbitLoopy")
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
		solution = 0
		for i in range(data):
			solution+=i
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
		solution = 0
		for i in range(data[0], data[1]):
			solution+=i
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
		solution = 0
		for i in range(data[0], data[1],2):
			solution+=i
		
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
		solution = []
		for s in data:
			solution.append(s.upper())
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
		solution = []
		for i in data:
			solution.append(i+20)
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
		solution = []
		for i,j in data:
			solution.append(j-1)
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
		solution = []
		for i,j in data:
			solution.append("".join([j,i]))
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
		solution = []
		for i in data:
			for j in i:
				solution.append(j.lower())
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
		solution = data[-1]
		data2 = data[:-1]
		for i in reversed(data2):
			solution-=i
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