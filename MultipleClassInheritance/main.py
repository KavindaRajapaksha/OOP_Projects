class Animal:
    def __init__(self, name):
        self.name = name

    def animal_info(self):
        print(f"I am an animal and my name is {self.name}")


class CanFly:
    def fly_animal(self):
        print(f"{self.name} can fly")

class CanWalk:
    def walk_animal(self):
        print(f"{self.name} can walk")

class Bird(Animal, CanFly):
    def __init__(self, name):
        Animal.__init__(self, name)

    def bird_info(self):
        print(f"I am a bird and my name is {self.name}")


pigeon = Bird("pigeon")
pigeon.animal_info()
pigeon.bird_info()
pigeon.fly_animal()