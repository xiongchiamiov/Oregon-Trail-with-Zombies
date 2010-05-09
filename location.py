from random import randint

# due to some circular dependencies, we have to define this class first before the other imports
class Location(object):
	pass

import city, river, field

def random_location():
	r = randint(0, 99)
	
	if r < 10:
		return city.random()
	elif r < 20:
		return river.random()
	else:
		return field.random()

