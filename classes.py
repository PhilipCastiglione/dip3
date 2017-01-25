class Car:
    '''totally a doc string - people love these apparently'''

    def __init__(self, wheels):
        self.wheels = wheels

    def horn(self):
        print("TOOT!")

    def class_horn():
        print("CLASS TOOT!")

    def wheel_count(self):
        print(self.wheels)

    def class_wheels():
        print(self.wheels)

c = Car(4)
c.horn()
c.wheel_count()
Car.class_horn()
# Car.class_wheels() # sweet error, self is not a thing, only a convention
