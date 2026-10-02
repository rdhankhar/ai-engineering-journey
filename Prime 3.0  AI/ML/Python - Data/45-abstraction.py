from abc import ABC , abstractmethod

class animal:
    
    @abstractmethod
    def make_sound(self):
        pass
    
class lion(animal):
    def make_sound(self):
        print("Roar!")
        
class cow(animal):
    def make_sound(self):
        print("Mooo!")
    
class dog(animal):
    def make_sound(self):
        print("Bark!")
        
l1 = lion()
print(l1.make_sound())

c1 = cow()
print(c1.make_sound())

b1 = dog()
print(b1.make_sound())