#!/usr/bin/python3

"""RIPSAW Server - Python 3.5
The RIPSAW server that hosts RIPSAW Games"""

import xml.etree.ElementTree as ET
import select, socketserver
from multiprocessing import Process

from ripsawServer import game, xmlLib

class RipsawServer:
	"""The RIPSAW Server is the base class for all RIPSAW servers. The server handles
	all requests from RIPSAW clients. Each RIPSAW server host a single RIPSAW game.
	The RIPSAW server is a mulithreaded server and can handle multiple requests. 
	The server itself runs as a daemon controlled by the overarching RIPSAW process"""
	
	server = None
	server_daemon = None

	class Handler(socketserver.BaseRequestHandler):
		"""The Handler class is responsible for handling all connections to teh RIPSAW
		server."""
		
		config = None
		banner = None
		game = None
		authorizedAcces = None
		requestHandler = None
		responseFactory = None
		
		def setup(self):
			"""Initializes all configurations for a connection"""
			self.config = self.server.config
			self.banner = self.config["banner"]
			self.game = game.Game(self.server.gamePath, self.config["flag"])
			self.authorizedAccess = False if "password" in self.config else True
			self.requestHandler = xmlLib.RequestHandler()
			self.responseFactory = xmlLib.ResponseFactory()
			
		def handleQuestion(self, xmlString):
			"""Handles requests for the question text"""
			levelText = self.game.getLevelText()
			response = self.responseFactory.generateQuestion(levelText)
			return response
		
		def handleData(self, xmlString):
			"""Handles requests for the question data"""
			levelData = self.game.getLevelData()
			response = self.responseFactory.generateData(levelData)
			self.request.sendall(response)
			
			answeredInTime = select.select([self.request], [], [], 2.0)
			if answeredInTime[0]:
				xmlString = self.request.recv(1024).strip()
				root = ET.fromstring(xmlString)
				requestType = root.get("classtype")
				handler = self.requestTypes.get(requestType)
				response = handler(self, xmlString)
			else:
				xmlString = self.request.recv(1024).strip()
				root = ET.fromstring(xmlString)
				requestType = root.get("classtype")
				if requestType == "answer":
					response = self.responseFactory.generateAnswer(False)
				else:
					handler = self.requestTypes.get(requestType)
					response = handler(self, xmlString)
			return response
		
		def handleAnswer(self, xmlString):
			"""Handles answer submissions for the question"""
			answer = self.requestHandler.handle(xmlString)
			answerCorrect = self.game.checkLevelAnswer(answer)
			response = self.responseFactory.generateAnswer(answerCorrect)
			return response
		
		def handlePassword(self, xmlString):
			"""Handles password submission for access"""
			password = self.requestHandler.handle(xmlString)
			if "password" in self.config:
				if password == self.config["password"]:
					self.authorizedAccess = True
				response = self.responseFactory.generatePassword(self.authorizedAccess)
			else:
				self.authorizedAccess = True
				response = self.responseFactory.generatePassword(self.authorizedAccess)
			return response
		
		requestTypes = {"question":handleQuestion, "data":handleData, "answer":handleAnswer, "password":handlePassword}
		
		def handle(self):
			"""The main handler for all requests"""
			xmlBanner = self.responseFactory.generateQuestion(self.banner)
			self.request.sendall(xmlBanner)
			while True:
				xmlString = self.request.recv(1024).strip()
				if xmlString:
					root = ET.fromstring(xmlString)
					requestType = root.get("classtype")
					if self.authorizedAccess or requestType == "password":
						handler = self.requestTypes.get(requestType)
						response = handler(self, xmlString)
					else:
						response = self.responseFactory.generatePassword(self.authorizedAccess)
					self.request.sendall(response)
				else:
					break

	class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
		"""The Server class is the actual server repsonsible for hosting RIPSAW games."""
		config = None
		gamePath = None
		allow_reuse_address = True
		
		
	def __init__(self, serverIP, gamePath, config):
		"""Constructor for the RIPSAW Server"""
		self.serverIP = serverIP
		self.gamePath = gamePath
		self.config = config
		self.server = self.Server((serverIP, int(config['port'])), self.Handler)
		self.server.config = config
		self.server.gamePath = gamePath
		self.server_daemon = Process(target=self.server.serve_forever, name=gamePath.split('.')[-1], daemon=True)
	
	def run(self):
		"""Run the RIPSAW server"""
		self.server_daemon.start()

	def stop(self):
		"""Shutdown the RIPSAW server"""
		self.server_daemon.terminate()
	
	def start(self):
		self.server_daemon = Process(target=self.server.serve_forever, name=self.gamePath.split('.')[-1], daemon=True)
		self.run()
			
	def restart(self):
		"""Restart the RIPSAW server"""
		self.stop()
		self.start()
		
	def getStatus(self):
		"""Return the status (is_alive) of the server"""
		return self.server_daemon.is_alive()
		
	def getPID(self):
		"""Get the process ID (PID) of the server"""
		return self.server_daemon.pid
		
	def getName(self):
		"""Get the name of the server"""
		return self.server_daemon.name
