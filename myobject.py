#fish
# state: color, weight, species, speed
# behaviours: swimming, eating, hiding

class Fish:

    def  __init__(self, color, weight, species, speed):

        self.color = color
        self.weight = weight
        self.species = species
        self.speed = speed

    def swimming(self):
        print("the fish swims at", self.speed, "MPH")

    def heavy(self):
        print("The fish weighs", self.weight, "kgs")

    def type(self):
        print("the fish species is", self.species, "and the color is", self.color)


object = Fish(color="brown", weight=200, species="tilapia", speed=120)

object.swimming()
object.heavy()
object.type()




