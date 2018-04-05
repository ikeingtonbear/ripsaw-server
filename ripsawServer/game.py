#!/usr/bin/python3

"""RIPSAW Game - Python 3.5
The RIPSAW game object"""

import importlib
import json
from random import choice

class Game:
	"""The Game class is the object which represents a RIPSAW Game.
	The Game object is repsonsible for managing everything related
	to the game. It manages the current level the client is on, returns
	the text and date for the current challenge, and also checks answer
	submissions from the client against the actual answer."""
	game = None
	flag = None
	levels = None
	currentLevel = None
	currentDate = None
	currentAnswer = None
	
	def __init__(self, gameMod, flag):
		"""Initialize the RIPSAW game"""
		self.game = importlib.import_module(gameMod)
		self.flag = flag
		self.levels = self.game.levels
		self.currentData = None
		self.currentAnswer = None
		self.currentLevel = self.levels[0]
		
	def getLevelText(self):
		"""Return the current level challenge text"""
		return self.currentLevel.get("text")
		
	def getLevelData(self):
		"""Return the current level challenge data"""
		self.currentData, self.currentAnswer = self.currentLevel.get("data")()
		return self.currentData
		
	def resetLevelData(self):
		"""Reset the current level's challenge data and answer"""
		self.currentData, self.currentAnswer = None, None
		
	def checkLevelAnswer(self, answer):
		"""Check a client's answer against the actual answer"""
		if answer is not None:
			answerCorrect = answer == self.currentAnswer
			if answerCorrect:
			
				if len(self.levels)==1:
					answerCorrect = "Flag: "+self.flag
				else:
					self.levels.pop(0)
					self.currentLevel = self.levels[0]
		else:
			answerCorrect = False	
	
		self.resetLevelData()
		
		return answerCorrect
