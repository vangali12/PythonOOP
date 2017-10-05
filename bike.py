class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print("Price: " + str(self.price))
		print("Max Speed: " + str(self.max_speed))
		print("Miles: " + str(self.miles))
		return self
	def ride(self):
		self.miles += 10
		print("Riding")
		return self
	def reverse(self):
		self.miles -= 5
		print("Reversing")
		return self


bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(400, "40mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(250, "40mph")
bike3.reverse().reverse().reverse().displayInfo()

# To prevent negative miles, we can prohibit the reverse function from being run if self.miles is less than 5 miles.

# All methods should return self, in case we choose to change the ordering around, but in the three instances above, we only need to write "return self" for the ride and reverse methods.