#polymerphism
class Animal:
    def speak(self):
        pass

class Tiger(Animal):
    def speak(self):
        return"Woofi"

class Max(Animal):
    def speak(self):
        return"bow.."

class Pelli(Animal):
    def speak(self):
        return"moo.."

def make_animal_speak(animal):
    print(animal.speak())

tiger=Tiger()
max=Max()
pelli=Pelli()

make_animal_speak(tiger)
make_animal_speak(max)
make_animal_speak(pelli)