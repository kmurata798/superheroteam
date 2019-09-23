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


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

"""
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):


class Hero:
    def __init__(self, name, starting_health):  # Starting health DEFAULT 100!!!
        self.name = name
        self.starting_health = starting_health

    def add_ability(ability):

    def attack(self):

    def defend(incoming_damage):

    def take_damage(damage):

    def is_alive(self):

    def fight(opponent):
        """
