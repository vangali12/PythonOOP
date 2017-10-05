class Store(object):
	def __init__(self, products, location, owner):
		self.products = products
		self.location = location
		self.owner = owner
	def add_product(self, newProduct):
		self.products.append(newProduct)
		return self
	def remove_product(self, removeProduct):
		self.products.remove(removeProduct)
		return self
	def inventory(self)
		