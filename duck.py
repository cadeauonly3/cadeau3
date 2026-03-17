class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
         print("meou")
def make_sound(obj):
    obj.sound()
make_sound(Dog())
make_sound(Cat())
    