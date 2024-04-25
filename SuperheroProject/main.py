class Superheros :
    def __init__(self,name,superpower):
        self.name = name
        self.superpower = superpower

    def use_power(self):
        print(f"{self.name} is using {self.superpower}")
    
    def intro_hero(self):
        print(f"{self.name} has the superpower of {self.superpower}")
    
    def save_city(self):
        print(f"{self.name} is saving the city")
    def power_level(self):
        length = len(self.superpower)
        level = length*10
        return level
    

class Flying(Superheros):
    def __init__(self,name,superpower,speed):
        super().__init__(name,superpower)
        self.speed = speed
    def use_power(self):
        print(f"{self.name} is using {self.superpower} and flying at {self.speed} mph")
    def calc_distance(self,flight_time):
        distance = self.speed*flight_time
        return distance
    
    
batman = Superheros("Batman","Money")
batman.use_power()
batman.intro_hero()
batman.save_city()
print(batman.power_level())

superman = Flying("Superman","Flight",1000)
superman.use_power()
superman.intro_hero()
superman.save_city()
print(superman.power_level())
print(superman.calc_distance(2))
        