class Patient(object):
	def __init__(self, identification, name, allergies):
		self.identification = identification
		self.name = name
		self.allergies = allergies
		self.bed = None
	def display(self):
		print("Identification: " + str(self.identification))
		print("Name: " + self.name)
		print("Allergies: " + self.allergies)
		print("Bed: " + str(self.bed))

class Hospital(object):
	def __init__(self, name, capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity
	def admit(self, person):
		self.patients.append(person)
		person.bed = len(self.patients)
		return self
	def discharge(self, person):
		for y in self.patients:
			if person.identification == y.identification:
				self.patients.remove(y)
		person.bed = None
		return self
	def display(self):
		print("Patients: ")
		for patients in self.patients:
			print(patients.__dict__)
		print("Capacity: " + str(self.capacity))
		print("Remaining Space: " + str(self.capacity - len(self.patients)))
		return self

sam = Patient(15543, "Sam", "Bananas")
#p1.display()
kevin = Patient(16848, "Kevin", "Latex")
#p2.display()

harborview = Hospital("Harborview", 280)
harborview.admit(sam).admit(kevin).discharge(sam).display()
sam.display()