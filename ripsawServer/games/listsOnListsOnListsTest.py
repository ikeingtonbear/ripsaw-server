#!/usr/bin/python3

from . import listsOnListsOnLists as testModule
from sys import exit

try:
	testLevels = testModule.levels
except:
	print("Unable to load levels from listsOnListsOnLists")
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
		solution = data[0]
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
		solution = data[-1]
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
		solution = data[4]
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
		solution = data[:3]
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
		solution = data[-3:]
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
		solution = data[3:-3]
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
		solution = data
		solution[3] = "HelloWorld"
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
		solution.insert(3, "HelloWorld")
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
		solution = data.append("HelloWorld")
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

def testLevel10():
	try:
		testLevel = testLevels[9]
	except:
		print("Unable to get testLevel[9]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[9] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data.remove("HelloWorld")
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
	
def testLevel11():
	try:
		testLevel = testLevels[10]
	except:
		print("Unable to get testLevel[10]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[10] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data.reverse()
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
	
def testLevel12():
	try:
		testLevel = testLevels[11]
	except:
		print("Unable to get testLevel[11]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[11] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data.sort()
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
	
def testLevel13():
	try:
		testLevel = testLevels[12]
	except:
		print("Unable to get testLevel[12]")
		return
		
	try:
		testLevelText = testLevel["text"]
		print(testLevelText)
	except:
		print("Unable to get testLevel[12] text")
		return
		
	try:
		testLevelFunction = testLevel["data"]
		testLevelData, testLevelSolution = testLevelFunction()
	except:
		print("Unable to get testLevel Data")
		return
	
	try:
		data = testLevelData
		solution = data[0].extend(data[1])
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
	      testLevel9,
	      testLevel10,
	      testLevel11,
	      testLevel12,
	      testLevel13]

def run():
	for tl in range(len(testLevels)):
		print("Testing level ",tl+1)
		tests[tl]()
		
if __name__ == "__main__":
	run()