class Product(object):
	def __init__(self, price, name, weight, brand, cost):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "sale"
	def sell(self):
		self.status = "sold"
		return self
	def addTax(self, tax):
		self.price = self.price + (self.price * tax)
		return self
	def returnItem(self, reason):
		if (reason is "defective"):
			self.status = "defective"
			self.price = 0
			return self
		if (reason is "new"):
			self.status = "sale"
			return self
		if (reason is "opened"):
			self.status = "used"
			self.price = float((self.price * 0.8))
			return self
	def displayInfo(self):
		print("Price: " + str(self.price))
		print("Name: " + self.name)
		print("Weight: " + self.weight)
		print("Brand " + self.brand)
		print("Cost: " + str(self.cost))
		print("Status: " + self.status)

#item1 = Product(21, "strawberries", "1lb", "Driscoll's", 5)
#item1.displayInfo()
#item1.sell().displayInfo()
#item1.addTax(0.1).displayInfo()
#item1.returnItem("defective").displayInfo()
#item1.returnItem("new").displayInfo()
#item1.returnItem("opened").displayInfo()