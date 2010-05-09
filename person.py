class Person(object):
	def __init__(self, name=None, age=None, gender=None):
		self.name = name
		self.age = age
		self.gender = gender
		self.hp = 10
		self.diseases = []
	
	def __str__(self):
		return "%s: %d" % (self.name, self.hp)
