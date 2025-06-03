# method_overriding/vehicle_example.py
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        return "Engine started"
    
    def stop_engine(self):
        return "Engine stopped"

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    
    # Overriding start_engine method
    def start_engine(self):
        return "Electric motor activated"
    
    # Overriding stop_engine method
    def stop_engine(self):
        return "Electric motor deactivated"

class HybridCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.fuel_capacity = fuel_capacity
    
    # Overriding start_engine method
    def start_engine(self):
        return "Hybrid system activated - using electric motor first"

# Usage
tesla = ElectricCar("Tesla", "Model S", 2023, 100)
print(tesla.start_engine())  # "Electric motor activated"

prius = HybridCar("Toyota", "Prius", 2023, 10, 45)
print(prius.start_engine())  # "Hybrid system activated..."