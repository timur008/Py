import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.society = 50
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def days_indexes(self):
        pass
    def is_alive(self):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength=brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

brands_list{
    "BMW"
    "Mercedes"
    "Skoda"
    "Lada"
    "Lamborghini"
    "Porsche"
}