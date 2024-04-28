class Country:
    def __init__(self,name,capital,population):
        self.name = name
        self.capital = capital
        self.population = population
    def get_info(self):
        return{
            "Name":self.name,
            "Capital":self.capital,
            "Population":self.population
        
        }
class DevelopedCountry(Country):
    def __init__(self,name,capital,population,gdp):
        super().__init__(name,capital,population)
        self.gdp = gdp

    def get_info(self):
        info=super().get_info()
        info["GDP"]=self.gdp
        return info
        
        

class DevelopingCountry(Country):
    def __init__(self,name,capital,population,unemployment_rate):
        super().__init__(name,capital,population)
        self.unemployment_rate = unemployment_rate

    def get_info(self):
        info=super().get_info()
        info["Unemployment Rate"]=self.unemployment_rate 
        return info
        

class World:
    def __init__(self):
        self.countries = []
    def add_country(self,country):
        self.countries.append(country)
    def get_all_countries(self):
        return [country.get_info() for country in self.countries]
    def get_country(self,name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None
    


world=World()

china = DevelopingCountry("China","Beijing",1400000000,4.3)
usa = DevelopedCountry("USA","Washington",300000000,20.5)
india = DevelopingCountry("India","New Delhi",1300000000,5.5)
uk = DevelopedCountry("UK","London",66000000,10.5)
world.add_country(china)
world.add_country(usa)
world.add_country(india)
world.add_country(uk)

print(world.get_all_countries())
