#!/usr/bin/env python

from random import randint

import city
from location import random_location
from person import Person

class GameSetup(object):
	class GameStartException(Exception):
		def __str__(self):
			return "Game setup completed."
	
	def __init__(self):
		self.render = self.cli
		self.game = Game()
	
	def run(self):
		try:
			while(True): self.render()
		except GameSetup.GameStartException, e:
			if self.game.path is None:
				self.game.path = [city.random()]
				self.game.path.extend([random_location() for i in range(0, randint(5, 10))])
				self.game.path.append(city.random())
			print e
		
		return self.game
	
	def cli(self):
		self.game.party = []
		while True:
			name = raw_input("Name: ")
			age = raw_input("Age: ")
			gender = raw_input("Gender (m/f): ")
			self.game.party.append(Person(name, age, gender))
			
			if raw_input("Would you like to add another member to your party? (Y/n): ") == 'n':
				break
		
		self.game.money = raw_input("How much money should we start you off with? ")
		
		raise GameSetup.GameStartException()

class Game(object):
	class GameEnd(Exception):
		pass
	
	def __init__(self, party=None, inventory=None, money=0, path=None, date=None, render=None):
		self.party = party
		self.inventory = inventory
		self.money = money
		self.path = path
		self.date = date
		self.render = render if render else self.cli
		
	def run(self):
		try:
			while(True): self.render()
		except Game.GameEnd, e:
			print "Game Over"
	
	def cli(self):
		#for person in self.party:
		#	print person
		#print " --> ".join([str(l) for l in self.path])
		
		commands = {}
		
		def _(args=[]):
			''' Displays more information about a command, or lists all commands. '''
			try:
				print commands[args[0]].__doc__
			except (IndexError, KeyError):
				print 'Available commands: ' + ' '.join(sorted(commands.keys()))
		commands['help'] = _
		
		def _(args=[]):
			''' Quits the game. '''
			raise Game.GameEnd()
		commands['quit'] = _
		
		command = raw_input('> ').strip().lower().split(' ')
		
		try:
			commands[command[0]](command[1:])
		except IndexError:
			commands[command[0]]
		except KeyError:
			commands['help']

if __name__ == '__main__':
	GameSetup().run().run()
