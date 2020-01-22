
from abc import ABC, abstractmethod
import wheel
#import abc

class Vehicle(ABC):
	__speed = 0
	__name = ''
	__color = ''
	__wheel = wheel.Wheel()

	def __init__(self):
		data = ''
		__speed = 0
		__name = ''
		__color = ''
	
	@abstractmethod
	def setName(self, n):
		#self.__name = n
		pass
	def getName(self):
		#return self.__name
		pass

	def setColor(self, c):
		#self.__color = c
		pass
	def getColor(self):
		pass
		#return self.__color

	def setSpeed(self, s):
		#self.__speed = s
		pass
	def getSpeed(self):
		#return self.__speed
		pass
	def brake(self):
		#self.__speed = 0
		pass


	

