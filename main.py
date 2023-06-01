print("пункт 1")

class Vehicle:
    def __init__(self, make, model, weight, year):
        self.make = make
        self.model = model
        self.weight = weight
        self.year = year
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, weight, year, num_doors, num_passengers):
        super().__init__(make, model, weight, year)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        return "The car's engine is starting..."

    def drive(self):
        return 'the car started moving'

a = Vehicle('audi', 'A7', 1860, 2014)
print(a.start_engine())

car = Car('audi', 'A7', 1860, 2014, 4, 4)
print(car.start_engine())
print(car.drive())

print("пункт 2")

class Truck(Vehicle):
    def __init__(self, make, model, weight, year, cargo_capacity, towing_capacity):
        super().__init__(make, model, weight, year)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        return "The truck's engine is starting..."
    def haul(self):
        print( f"Фірма {self.make}, Модель {self.model}, Вага {self.weight}, Рік {self.year}", \
               f"Вантажопідйомність {self.cargo_capacity}, Макс.вага {self.towing_capacity}")
truck=Truck('mercedes-benz', 'actros', '9000.', 2013, '26000.', '40000')
truck.haul()
print(truck.start_engine())

print("пункт 3")

class Motorcycle(Vehicle):
    def __init__(self, make, model, weight, year, num_wheels, has_sidecar):
        super().__init__(make, model, weight, year)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return "The motorcycle's engine is starting..."

    def ride(self):
        print( f"Фірма {self.make}, Модель {self.model}, Вага {self.weight}, Рік {self.year}", \
               f"Кількість колес {self.num_wheels}, Має коляску {self.has_sidecar}")
motorcycle=Motorcycle('mercedes-amg', 'agusta f3 800', '173.', 2021, '2', 'немає')

print(motorcycle.start_engine())
motorcycle.ride()

print(car.start_engine())
print(truck.start_engine())
print(motorcycle.start_engine())
print(a.start_engine())