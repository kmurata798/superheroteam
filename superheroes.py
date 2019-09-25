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
        self.kills = 0
        self.deaths = 0


# if __name__ == "__main__":
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

    def add_kills(self, num_kills):
        self.kills = num_kills

    def add_deaths(self, num_deaths):
        self.deaths = num_deaths

    def add_ability(self, ability):
        self.abilities.append(ability)

    def hero_stats(self):
        print(self.name, ": ")
        if self.deaths == 0:
            kdRatio = self.kills // self.deaths
            print(
                f"has {self.kills} kills and {self.deaths} deaths! KD Ratio = {kdRatio}")
        else:
            print(
                f"has {self.kills} kills and NO deaths! KD Ratio = {kdRatio}")

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

    def defend(self, damage_amt=0):
        total = 0
        for piece in self.armors:
            total += piece.block()
        # return total  #returns ONLY YOUR BLOCK DAMAGE
        return abs(damage_amt - total)


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
        current_health = self.current_health
        final_damage = self.defend(damage)
        self.current_health = current_health - final_damage


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.name)
#     print(hero.current_health)

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
                self.kills += 1
                opponent.deaths += 1
                print(self.name, "won!")
            elif opponent.is_alive() == True:
                opponent.kills += 1
                self.deaths += 1
                print(opponent.name, "won!")

                # if __name__ == "__main__":
                #     # If you run this file from the terminal
                #     # this block is executed.

                #     hero = Hero("Grace Hopper", 200)
                #     hero.take_damage(150)
                #     print(hero.is_alive())
                #     hero.take_damage(15000)
                #     print(hero.is_alive())


class Weapon(Ability):

    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    ''' Initialize your team with its team name
    '''
    # Implement this constructor by assigning the name and heroes, which should be an empty list

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return 0
        # Implement this method to remove the hero from the list given their name.

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal.

    def attack(self, other_team):
        for hero in self.heroes:
            for enemy in other_team.heroes:
                while hero.is_alive() == True and enemy.is_alive() == True:
                    hero.take_damage(enemy.attack())
                    enemy.take_damage(hero.attack())
                    if hero.is_alive() == False:
                        self.heroes.remove(hero)
                    elif enemy.is_alive() == False:
                        other_team.heroes.remove(enemy)

    def revive(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        print("\n|| Team Statistics ||")
        for hero in self.heroes:
            hero.hero_stats()
