#!/usr/bin/python3

"""RIPSAW - Python 3.5

RIPSAW reads configurations for the server from ripsaw.conf. The configurations
are used to set up the server option and also all the RIPSAW game options. See
ripsaw.conf for all the options available and how to set up the RIPSAW games.

Each RIPSAW game is hosted by a multi-threaded server so that it can handle multiple
requests. Each server that hosts a game is run as a daemon. Type 'Yes' to stop all 
RIPSAW servers.

Future iterations will have the possibility to start, stop and restart specific servers"""

import configparser
from sys import exit#RIPSAW imports
from subprocess import call

from ripsawServer import server

serverList = []
def setup():
	configs = configparser.ConfigParser()
	configs.read('ripsaw.conf')
	games = [game.strip() for game in configs['ServerOpts']['games'].split(',')]
	gameDir = configs['ServerOpts']['gameDir']
	serverIP = configs['ServerOpts']['serverIP']

	for game in games:
		gameMod = '.'.join((gameDir, game))
		s = server.RipsawServer(serverIP, gameMod, configs[game])
		serverList.append(s)
		s.run()
		#print("%s server started." % s.getName())

def _printOptions():
	"""Print the available option"""
	options=["View servers", "View server statuses", "View server PIDS", "Stop a server", "Start a server", "Restart a server", "Shutdown RIPSAW"]
	for i, option in enumerate(options):
		print('[',i,'] ', option)
		
def _handleSelection(opt):
	"""Handle the user's selection"""
	if opt==0:
		"""View servers"""
		for i, server in enumerate(serverList):
			print(i," ", server.getName())
	elif opt==1:
		"""View statuses"""
		for i, server in enumerate(serverList):
			print(i," ", server.getName(),"-","Running " if server.getStatus() else "Stopped")
		
	elif opt==2:
		"""View PIDS"""
		for i, server in enumerate(serverList):
			print(i," ", server.getName(),"-",server.getPID())
	
	elif opt==3:
		"""Stop server"""
		for i, server in enumerate(serverList):
			print("[",i,"] ", server.getName())
			
		print()
		selection = int(input("Select a server to stop: "))
		serverList[selection].stop()
		
	elif opt==4:
		"""Start server"""
		#pass
		for i, server in enumerate(serverList):
			print("[",i,"] ", server.getName())
			
		print()
		selection = int(input("Select a server to start: "))
		serverList[selection].start()
		
	elif opt==5:
		"""Restart server"""
		#pass
		for i, server in enumerate(serverList):
			print("[",i,"] ", server.getName())
			
		print()
		selection = int(input("Select a server to restart: "))
		serverList[selection].restart()

	elif opt==6:
		"""Shutdown RIPSAW"""
		for server in serverList:
			server.stop()
			
		exit()
	else:
		print("Invalid option")

def maintain():	
	while True:
		#call("clear")
		_printOptions()
		opt = int(input("Select an option: "))
		print()
		_handleSelection(opt)
		print()
		
	

if __name__ == "__main__":
	setup()
	maintain()