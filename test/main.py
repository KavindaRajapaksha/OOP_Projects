class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person({self.name})"
    
person = Person("John")
print(person)