class Call(object):
	def __init__(self, identification, name, phone, time, reason):
		self.identification = identification
		self.name = name
		self.phone = phone
		self.time = time
		self.reason = reason
	def display(self):
		print("ID: " + str(self.identification))
		print("Name: " + self.name)
		print("Phone: " + str(self.phone))
		print("Time: " + str(self.time))
		print("Reason: " + self.reason)


class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queueSize = 0
	def add(self, call):
		self.calls.append(call)
		self.queueSize += 1
		return self
	def remove(self):
		del self.calls[0]
		self.queueSize -= 1
		return self
	def display(self):
		print("List of Calls: ")
		for call in self.calls:
			print(call.__dict__)
		print("Queue Size: " + str(self.queueSize))


c1 = Call(1216843, "Sam", "444-444-4444", 1730, "Defective Product")
# c1.display()
c2 = Call(154651, "Kevin", "555-555-5555", 0300, "Product Praise")
# c2.display()

center1 = CallCenter()
# center1.display()
center1.add(c1).add(c2).display()
#center1.add(c1).add(c2).remove().display()