# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# class Vehicle:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = name

# class FlightVehicle(Vehicle):
#     def __init__(self, name, type, model):
#         super().__init__(self, name, type)
#         self.model = model

# class Starship(FlightVehicle):
#     def __init__(self, name, type, model):
#         super().__init__(self,name,type,model)

# class Airplane(FlightVehicle):
#     def __init__(self, name, type, model):
#         super().__init__(self,name,type,model)

# class GroundVehicle(Vehicle):
#     def __init__(self, name, type, model, number_of_wheels):
#         super().__init__(self, name, type)
#         self.model = model
#         self.number_of_wheels = number_of_wheels

# class Car(GroundVehicle):
#     def __init__(self, name, type, model, number_of_wheels):
#         super().__init__(self, name, type, model, number_of_wheels)

# class Motorcycle(GroundVehicle):
#     def __init__(self, name, type, model, number_of_wheels):
#         super().__init__(self, name, type, model, number_of_wheels)

class Vehicle:
    	pass

class GroundVehicle(Vehicle):
	pass

class Car(GroundVehicle):
	pass

class Motorcycle(GroundVehicle):
	pass

class FlightVehicle(Vehicle):
	pass

class Airplane(FlightVehicle):
	pass

class Starship(FlightVehicle):
	pass



