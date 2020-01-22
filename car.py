import engine
import vehicles

class Car(vehicles.Vehicle):
	pass
	__engine = engine.Engine()
	__speed = 0
	__name = ''
	__color = ''

	def __init__(self, n):
		vehicles.Vehicle.__init__(self)
		self.data = "" 
		self.__name = n
		self.__wheels = 4
		self.__speed = 0

	def start(self):
		#print("setting car speed")
		#setSpeed(self, 15)
		self.__speed = 15

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

		

