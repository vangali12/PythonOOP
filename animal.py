class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print("Animal Health: " + str(self.health))
		return self


class Dog(Animal):
	def __init__(self, name, health):
		super(Dog, self).__init__(name, health)
		self.health = 150
	def pet(self):
		self.health += 5
		return self
class Dragon(Animal):
	def __init__(self, name, health):
		super(Dragon, self).__init__(name, health)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		super(Dragon, self).displayHealth()
		print("I am a Dragon")

buddy = Dog("Buddy", 180)
simon = Dragon("Simon", 100)

buddy.walk().displayHealth() # should display 149
simon.fly().displayHealth() # should display 160

buddy.fly().displayHealth() # should throw an error becuase dogs can't fly