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
        self.current_health = 100


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
            # added the total damage taken after you block the damage
            total_taken = damage_amt - total
        # return total  #returns ONLY YOUR BLOCK DAMAGE
        return total_taken


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    armor = Armor("shield", 20)
    another_armor = Armor("bigger shield", 30)
    hero = Hero("Marty Metoo", 180)
    hero.add_armor(armor)
    hero.add_armor(another_armor)
    print(hero.defend(40))

"""
    def take_damage(damage):

    def is_alive(self):

    def fight(opponent):
"""
