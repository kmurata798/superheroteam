import dog

my_dog = dog.Dog("Rex", "SuperDog")
#my_dog.breed = "SuperDog"
my_dog.bark()
my_other_dog = dog.Dog("Annie", "SuperDog")
my_other_dog2 = dog.Dog("boy", "WackyDog")
my_other_dog3 = dog.Dog("boyoy", "PartyDog")
print(my_other_dog.name)
my_other_dog.sit()
print(my_other_dog2.name)
my_other_dog2.rollover()
print(my_other_dog3.name)
my_other_dog3.rollover()

dog.greeting = "Woah"
my_dog.bark()
my_other_dog.bark()
my_other_dog2.bark()
my_other_dog3.bark()
