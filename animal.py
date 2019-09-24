class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))

    def eat(self):
        print(self.name, "began eating!")

    def drink(self):
        print(self.name, "began drinking!")


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()
my_dog.eat()
my_dog.drink()
