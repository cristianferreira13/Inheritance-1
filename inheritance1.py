class Cars:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
class Sedan(Cars):
    def __init__(self, brand, year, capacity, fuel):
        super().__init__(brand,year)
        self.capacity = capacity
        self.fuel = fuel
        
class Suv(Cars):
    def __init__(self, brand, year, wheels, passengers):
        super().__init__(brand, year)
        self.wheels = wheels
        self.passengers = passengers
        
class Luxury(Cars):
    def __init__(self, brand,year, materials, price):
        super().__init__(brand, year)
        self.materials = materials
        self.price = price