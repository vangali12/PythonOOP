class MathDojoIneff(object):
	def __init__(self, value):
		self.value = value
	def add(self, *nums):
		if (len(nums) < 2):
			total = nums[0]
		else:
			total = 0
			for i in range(0, len(nums)):
				total += nums[i]
		self.value += total
		return self
	def subtract(self, *nums):
		if (len(nums) < 2):
			total = nums[0]
		else:
			total = 0
			for i in range(0, len(nums)):
				total += nums[i]
		self.value -= total
		return self
	def result(self):
		print(self.value)



class MathDojo(object):
	def __init__(self, value):
		self.value = value
	def add(self, *nums):
		lists = [nums]
		total = (map(sum, lists))[0]
		self.value += total
		return self
	def subtract(self, *nums):
		lists = [nums]
		total = (map(sum, lists))[0]
		self.value -= total
		return self
	def result(self):
		print(self.value)

# The "sequence" element in the map function has to be iterable, but for some reason a simple tuple doesn't seem to be iterable. Python thinks that a tuple is an "int" object. In order to get around this problem, I put the tuple into a list, this way it was able to iterate over the items inside the tuple contained within the list. WHY IS THIS?!?!?!?!?!?!

md = MathDojo(0)

# md.add(2,5).result()
# md.add(2).add(2,5).subtract(3,2).result()

class MathDojoTwo(object):
	def __init__(self, value):
		self.value = value
	def add(self, *nums):
		new_list = []
		for i in nums:
			if type(i) is list:
				new_list.append(sum(i))
			else:
				new_list.append(i)
		self.value += sum(new_list)
		return self
	def subtract(self, *nums):
		new_list = []
		for i in nums:
			if type(i) is list:
				new_list.append(sum(i))
			else:
				new_list.append(i)
		self.value -= sum(new_list)
		return self
	def result(self):
		print(self.value)

nd = MathDojoTwo(0)

nd.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()