# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " said Woof!")

    def sit(self):
        print(self.name + " <> Sit")

    def rollover(self):
        print(self.name + " <> Roll over")
