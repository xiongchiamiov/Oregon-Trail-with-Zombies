from random import choice, randint

from location import Location

RIVER_NAMES = ['Back Creek', 'Back River', 'Bad River', 'Bad River',
               'Bad Axe River', 'Baker River', 'Baker River', 'Baker Brook River',
               'Bald River', 'Bald Eagle Creek', 'Ballona Creek', 'Banister River',
               'Baraboo River', 'Baranof River', 'Bark River', 'Bark River',
               'Bark River', 'Barnes Creek', 'Barren River', 'Barren Fork River',
               'Barrington River', 'Barton Creek', 'Barton River', 'Bass River',
               'Bass River', 'Batsto River', 'Batten Kill', 'Battle Creek River',
               'Baudette River', 'Bayou des Arc', 'Bayou des Cannes',
               'Bayou Macon', 'Bayou Manchac', 'Bayou Nezpique',
               'Bayou Plaquemine Brule', 'Bayou Queue de Tortue', 'Bayou Teche',
               'Bayou Wikoff']

def random():
	return River(choice(RIVER_NAMES), randint(5, 300)/10.0, randint(5, 50), randint(1, 30))

class River(Location):
	def __init__(self, name, depth=1.0, width=5, strength=1):
		self.name = name
		self.depth = depth
		self.width = width
		self.strength = strength
	
	def __str__(self):
		return self.name
	
	def greeting(self):
		return "A moving mass of water!  It's %s!" % self.name
