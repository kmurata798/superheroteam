import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """
        Hero's ability damage
        """
        return random.randint(1, self.max_damage)

# TESTING
# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(1, self.max_block)


# TESTING
# if __name__ == "__main__":
#     armor = Armor("Big Boy Armor", 50)
#     print(armor.name)
#     print(armor.block())


class Hero:
    def __init__(self, name, starting_health=100):  # Starting health DEFAULT 100!!!
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health


# if __name__ == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

    def add_ability(self, ability):
        self.abilities.append(ability)


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     ability2 = Ability("Sneaky Hacky", 75)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(ability2)
#     print(hero.abilities)


    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())


    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total = 0
        for piece in self.armors:
            total += piece.block()
        # return total  #returns ONLY YOUR BLOCK DAMAGE
        return damage_amt - total


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     armor = Armor("shield", 20)
#     another_armor = Armor("bigger shield", 30)
#     hero = Hero("Marty Metoo", 180)
#     hero.add_armor(armor)
#     hero.add_armor(another_armor)
#     print(hero.defend(40))

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.name)
    print(hero.current_health)

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.abilities == None and opponent.abilities == None:
            print("DRAW!!!")

        else:
            if self.is_alive() == True:
                print(self.name, "won!")
            elif opponent.is_alive() == True:
                print(opponent.name, "won!")

                # if __name__ == "__main__":
                #     # If you run this file from the terminal
                #     # this block is executed.

                #     hero = Hero("Grace Hopper", 200)
                #     hero.take_damage(150)
                #     print(hero.is_alive())
                #     hero.take_damage(15000)
                #     print(hero.is_alive())


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
