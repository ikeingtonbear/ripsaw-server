#!/usr/bin/python3

"""RIPSAW XML - Python 3.5
Handles the parsing and generation of RIPSAW XML"""

import xml.etree.ElementTree as ET
import json

questionType = "question"
dataType = "data"
answerType = "answer"
passwordType = "password"

class RequestHandler:
	"""The RequestHandler class is repsonsible for parsing all XML requests fromstring
	the RIPSAW client"""
	
	def handleQuestion(self, root):
		"""Handle the XML for the request for question text"""
		return True
	
	def handleData(self, root):
		"""Handle the XML for the request for question data"""
		return True
	
	def handleAnswer(self, root):
		"""Handle the XML for the and answer submission"""
		jsonAnswer = root.findtext("answer")
		answer = json.loads(jsonAnswer)
		return answer
	
	def handlePassword(self, root):
		"""Handle the XML for the request for a password submission"""
		jsonPassword = root.findtext("password")
		password = json.loads(jsonPassword)
		return password
	
	requestTypes = {questionType:handleQuestion, dataType:handleData, answerType:handleAnswer, passwordType:handlePassword}
	
	def handle(self, xmlString):
		"""Handle all XML from requests"""
		xmlRoot = ET.fromstring(xmlString)
		requestType = xmlRoot.get("classtype")
		return self.requestTypes.get(requestType)(self, xmlRoot)
	
	
class ResponseFactory:
	
	xmlTypes = {questionType:"question", dataType:"data", answerType:"answer", passwordType: "password"}

	def generateBase(self, XMLTYPE):
		"""Create the base RIPSAW XML"""
		baseXML = ET.Element("RIPSAW", classtype=XMLTYPE)
		return baseXML
	
	def generateQuestion(self, questionText):
		"""Create the XML to return question text"""
		baseXML = self.generateBase(self.xmlTypes.get(questionType))
		questionXML = ET.SubElement(baseXML, "questionText")
		questionXML.text = json.dumps(questionText)
		return ET.tostring(baseXML)
	
	def generateData(self, data):
		"""Create the XML to return question data"""
		baseXML = self.generateBase(self.xmlTypes.get(dataType))
		dataXML = ET.SubElement(baseXML, "data")
		dataXML.text = json.dumps(data)
		return ET.tostring(baseXML)
	
	def generateAnswer(self, answerCorrect):
		"""Create the XML to return the result of an answer submission"""
		answerText = "Incorrect. Try again."
		if answerCorrect==True:
			answerText = "Correct! Level unlocked!"
		elif answerCorrect:
			answerText = answerCorrect
		baseXML = self.generateBase(self.xmlTypes.get(answerType))
		answerXML = ET.SubElement(baseXML, "answer")
		answerXML.text = json.dumps(answerText)
		return ET.tostring(baseXML)
	
	def generatePassword(self, authorized):
		"""Create the XML to return the result of an password submission"""
		passwordText = "Access denied"
		if authorized:
			passwordText = "Access granted"
		
		baseXML = self.generateBase(self.xmlTypes.get(passwordType))
		passwordXML = ET.SubElement(baseXML, "password")
		passwordXML.text = json.dumps(passwordText)
		return ET.tostring(baseXML)
