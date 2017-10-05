class User(object):
	def __init__(self, fName, lName, age):
		self.fName = fName
		self.lName = lName
		self.age = age
		self.identification = None
	def display(self):
		print("First Name: " + self.fName)
		print("Last Name: " + self.lName)
		print("Age: " + str(self.age))

class Userdb(object):
	def __init__(self, name):
		self.name = name
		self.dataBase = []
		self.currentCopy = []
	def create(self, person):
		person.identification = len(self.dataBase) + 1
		self.dataBase.append(person)
		return self
	def all(self):
		self.currentCopy = []
		for y in self.dataBase:
			self.currentCopy.append(y.__dict__)
		for items in self.currentCopy:
			print(items)
		return self
	def get(self, number):
		self.currentCopy = []
		for y in self.dataBase:
			if number == y.identification:
				self.currentCopy.append(y.__dict__)
				print(self.currentCopy)
		if not self.currentCopy:
			raise IndexError("This ID does not exist")
		return self
	def filter(self, **kwargs):
		self.currentCopy = []
		for y in self.dataBase:
			for key, value in kwargs.items():
				if value == getattr(y, key):
					self.currentCopy.append(y.__dict__)
		print(self.currentCopy)
	def exclude(self, **kwargs):
		self.currentCopy = []
		for y in self.dataBase:
			for key, value in kwargs.items():
				if value != getattr(y, key):
					self.currentCopy.append(y.__dict__)
		print(self.currentCopy)


alisa = User("Alisa", "VanGrunsven", 23)
christen = User("Christen", "Miyasato", 23)
hannah = User("Hannah", "Alcoba", 25)
marc = User("Marc", "Wai", 24)

db = Userdb("MyFavoritePeople")

# db.create(alisa).create(christen).create(hannah).create(marc).get(12) ## Should throw IndexError
# db.create(alisa).create(christen).create(hannah).create(marc).filter(age=23) ## Should display Alisa and Christen
# db.create(alisa).create(christen).create(hannah).create(marc).exclude(age=23) ## Should display Hannah and Marc
# db.create(alisa).create(christen).create(hannah).create(marc).all()
# db.create(alisa).create(christen).create(hannah).create(marc).get(4) ## Should display Marc