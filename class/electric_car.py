class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' '+self.make + ' '+self.model
        return long_name.title()

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")

    def fill_gas_tank(self):
        print("Gas filling")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size)+" kwh battery")

    def fill_gas_tank(self):
        print("This car doesnt need gas")


my_tesla = ElectricCar('tesla', 't4', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
