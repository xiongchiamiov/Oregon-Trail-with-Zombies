from random import choice, randint

from location import Location

CITY_NAMES = ['Adelanto', 'Agoura Hills', 'Alameda', 'Alamo', 'Albany', 'Alhambra',
              'Aliso Viejo', 'Alondra Park', 'Alpine', 'Alta Sierra', 'Altadena',
              'Alum Rock', 'American Canyon', 'Anaheim', 'Anderson', 'Antioch',
              'Apple Valley', 'Aptos', 'Arcadia', 'Arcata', 'Arden-Arcade',
              'Arroyo Grande', 'Artesia', 'Arvin', 'Ashland', 'Atascadero',
              'Atherton', 'Atwater', 'Auburn', 'August', 'Avenal',
              'Avocado Heights', 'Azusa']

def random():
	return City(choice(CITY_NAMES), randint(0, 10000))

class City(Location):
	def __init__(self, name, population=0, stores=[]):
		self.name = name
		self.population = population
		self.stores = stores
	
	def __str__(self):
		return self.name
