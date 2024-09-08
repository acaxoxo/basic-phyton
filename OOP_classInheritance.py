# OOP - Class Inheritance

class Car:
  def __init__(self):
    self.wheels = 4
    self.seats = 5
  def drive(self):
    print("Driving a car...")
    
myCar = Car()
myCar.drive()

###

class SportsCar(Car):
  def __init__(self):
    super().__init__()
    self.engine_power = '400 HP'
    self.seats = 2
    
  def drive(self):
    print("Driving a sports car...")
    
mySportsCar = SportsCar()
mySportsCar.drive()

###

class SportsCar(Car):
  def __init__(self):
    super().__init__()
    self.engine_power = '400 HP'
    self.seats = 2
    
mySportsCar = SportsCar()
mySportsCar.drive()