pet1 = {'name': 'frankie', 'age': 5, 'fur': 'gold'}
pet2 = {'name': 'Sal', 'age': '6 months', 'fur': 'scales'}
pet3 = {'name': 'Soleil', 'age': 2, 'fur': 'white'}

class Pet(object):
	def __init__(self, name, age, fur):
		self.name = name
		self.age = age
		self.fur = fur
		self.legs = 4

pet4 = Pet('Tina', 0.1, 'blue')

# print pet4.name
# print pet4.age

# pet4.legs = 3

class Vehicle(object):
	def __init__(self, color, typeOf, speed, noise):
		self.color = color
		self.type = typeOf
		self.speed = speed
		self.noise = noise
	def honk(self):
		print(self.noise)
		return self

v1 = Vehicle("red", "car", "15mph", "beep")
# v1.honk()

class Fighter(object):
	def __init__(self, name, health, attack):
		self.name = name
		self.health = health
		self.attack = attack
	def hit(self, otherFighter):
		otherFighter.health -= self.attack
		print ('You attacked {} for {} damage.').format(otherFighter.name, self.attack)

f1 = Fighter("Ray Bell", 960, 7)
f2 = Fighter("Michael Choi", 100000, 6)

f1.hit(f2)