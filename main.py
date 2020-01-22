import car
import bicycle

class Main:
	def __init__(self):
		wayne = car.Car("Ford Pinto")
		garth = bicycle.Bicycle("BMX")

		wayne.setColor("Blue")
		print("Wayne's " + wayne.getName() + " is " + wayne.getColor())

		wayne.start()
		print ("Wayne's speed is ", wayne.getSpeed())
		
		garth.pedal()
		print("Garth's speed is " , garth.getSpeed())

		garth.pedal()
		print("Garth's speed is " , garth.getSpeed())

		garth.brake()
		print("Garth's speed is " , garth.getSpeed())
		

		print(wayne.getName())
		print(garth.getName())


# Program Start 		
x = Main()

