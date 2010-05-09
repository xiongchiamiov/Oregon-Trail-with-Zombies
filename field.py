from random import randint

from location import Location

def random():
	r = randint(0, 99)
	
	if r < 25:
		return Desert()
	elif r < 75:
		return Plain()
	else:
		return Hills()

class Field(Location):
	pass

class Desert(Field):
	def __str__(self):
		return "desert"

class Plain(Field):
	def __str__(self):
		return "plain"

class Hills(Field):
	def __str__(self):
		return "hills"
