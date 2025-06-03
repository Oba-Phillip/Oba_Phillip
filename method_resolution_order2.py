# method_resolution_order/animal_hierarchy.py
class Animal:
    def speak(self):
        return "Some generic animal sound"

class Mammal(Animal):
    def speak(self):
        return "Mammal sound"

class Bird(Animal):
    def speak(self):
        return "Chirp"

class Dog(Mammal):
    def speak(self):
        return "Woof!"

class Platypus(Mammal, Bird):
    def speak(self):
        # Try Mammal first, then Bird, then Animal
        for base in [Mammal, Bird, Animal]:
            try:
                return super(base, self).speak()
            except:
                continue
        return "No sound"

# MRO demonstration
print(Platypus.__mro__)
# Output: (<class '__main__.Platypus'>, <class '__main__.Mammal'>, 
#          <class '__main__.Bird'>, <class '__main__.Animal'>, 
#          <class 'object'>)

perry = Platypus()
print(perry.speak())  # Uses Mammal's implementation ("Mammal sound")