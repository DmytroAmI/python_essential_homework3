class Car:
    """Describe and model a car"""
    def __init__(self, make, model, year, vin):
        """Initialize the attributes of the car"""
        self.__make = make
        self.__model = model
        self.__year = year
        self.__vin = vin

    def get_make(self):
        """getter"""
        return self.__make

    def get_model(self):
        """getter"""
        return self.__model

    def get_year(self):
        """getter"""
        return self.__year

    def get_vin(self):
        """getter"""
        return self.__vin

    def set_make(self, make):
        """setter"""
        self.__make = make

    def set_model(self, model):
        """setter"""
        self.__model = model

    def set_year(self, year):
        """setter"""
        self.__year = year

    def set_vin(self, vin):
        """setter"""
        self.__vin = vin

    def __str__(self):
        """Return a string representation of the car"""
        return f'{self.__make} {self.__model}, {self.__year}, vin: {self.__vin}'


car = Car("Ford", "Scorpio", 1990, "14234FRGREGRGUHFF")
print(car)

print(car.get_make())
print(car.get_model())

car.set_year(1991)
car.set_vin("64567EIHGRISDCAF")
print(car)
