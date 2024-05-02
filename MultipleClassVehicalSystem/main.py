class Vehicle:
    def __init__ (self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_vehicle(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class ElectricalVehicle():
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def display_battery(self):
        print(f"Battery Size: {self.battery_size}")
    def get_range(self):
        print(f"Range: {self.battery_size * 3}")

class GasolineVehicle():
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def display_fuel_capacity(self):
        print(f"Fuel Capacity: {self.fuel_capacity}")
    def get_range(self):
        print(f"Range: {self.fuel_capacity * 2}")


class HybridCar(Vehicle, ElectricalVehicle, GasolineVehicle):
    def __init__(self, make, model, year, battery_size, fuel_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricalVehicle.__init__(self, battery_size)
        GasolineVehicle.__init__(self, fuel_capacity)

    def display_hybrid_car(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Battery Size: {self.battery_size}, Fuel Capacity: {self.fuel_capacity}")


hybrid_car = HybridCar("Toyota", "Prius", 2019, 100, 10)
hybrid_car.display_vehicle()
hybrid_car.display_battery()
hybrid_car.display_fuel_capacity()
hybrid_car.display_hybrid_car()

