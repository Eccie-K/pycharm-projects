#object oriented programming.
#Real objects: car,iron box,person,phone, bike
# objects have states and behaviours
# states of a car: color, height, years, wheels, type,make,model
#behaviour(what the object does), speed, hoot, skid, sound
# in programming states = properties, behaviours = functions
# class can contain states and behavoiurs

class Car:
    def __init__(self, color, height, age, wheels, make, cost, speed): #states
        self.color = color
        self.height = height
        self.age = age
        self.wheels = wheels
        self.make = make
        self.cost = cost
        self.wheels = wheels
        self.speed = speed

    def move(self): #behaviours
        print("the car is moving")
        print("the car has new", self.wheels)
        print("the color is", self.color)
        print("it moves at", self.speed, "KPH")


    def skidding(self): #behaviours
        print("the car is skidding with", self.wheels, "wheels")


    def racing(self):
        print("the car is racing at", self.speed, "KPH")

object = Car(color = "black", wheels = 4, speed = "80", make = "BMW", age = 4, height = 1.2, cost = 5000000)
object.move()
object.skidding()
object.racing()

#.(dot) notation means accessing behaviours of objects/applying an attribute to an object
# above object has states and behaviours

