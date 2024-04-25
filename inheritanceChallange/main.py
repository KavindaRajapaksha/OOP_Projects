
#super class

class Animal:
    def __init__(self,region,animal_type,color,lethal):
        self.region=region
        self.animal_type=animal_type
        self.color=color
        self.lethal=lethal

    def animal_bio(self):
        print("Animal Passport:")
        print(f"Region: {self.region}")
        print(f"Animal Type: {self.animal_type}")
        print(f"Color: {self.color}")
        print(f"Lethal: {self.lethal}")

#sub class
class Clinic(Animal):
    def animal_info(self):
        print(f"This is a {self.animal_type} from {self.region}")

    def search(self,animals):
        region=input("Enter the region of the animal you are looking for: ").lower()
        for animal in animals:
            if animal.region==region:
                print(f"Animal found: {animal.animal_type} from {animal.region}")
                break
        else:
            print("Animal not found")

animals=[]
num_animals=int(input("Enter the number of animals: "))
for i in range(num_animals):
   region=input("Enter the region of the animal: ").lower()
   animal_type=input("Enter the type of animal: ").lower()
   color=input("Enter the color of the animal: ").lower()
   lethal=input("Is the animal dangerous? ").lower()
   lethal=lethal=="yes"
   animal=Animal(region,animal_type,color,lethal)
   animals.append(animal)

clinic=Clinic("africa","lion","yellow","yes")
clinic.animal_bio()
clinic.animal_info()
   



 