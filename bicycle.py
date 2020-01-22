import vehicles

class Bicycle(vehicles.Vehicle):
	__speed = 0
	__name = ''
	__color = ''

	def __init__(self, n):
		self.data = ""
		self.__name = n
		self.__wheels = 2

	def pedal(self):
		self.__speed += 5
	def setName(self, n):
		self.__name = n
	def getName(self):
		return self.__name

	def setColor(self, c):
		self.__color = c
	def getColor(self):
		return self.__color

	def setSpeed(self, s):
		self.__speed = s
	def getSpeed(self):
		return self.__speed
	def brake(self):
		self.__speed = 0

