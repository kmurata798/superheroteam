import random
from random import choice


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


    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.

    def add_armor(self, armor):
        '''Add Armor to self.armors
            armor: Armor Object
        '''
        self.armors.append(armor)
        # This method will add the armor object that is passed in to
        # the list of armor objects defined in the constructor: `self.armors`.

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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
        return self.current_health > 0

    def fight(self, opponent):
        if (len(self.abilities) + len(opponent.abilities)) > 0:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive():
                self.add_kills(1)
                opponent.add_deaths(1)
                print(self.name, "won!")

            elif opponent.is_alive():
                opponent.add_kills(1)
                self.add_deaths(1)
                print(opponent.name, "won!")

            else:
                print("DRAW")
                self.add_kills(1)
                opponent.add_deaths(1)
                opponent.add_kills(1)
                self.add_deaths(1)
        else:
            print("draw")

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
        self.heroes = []
        self.name = name

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

    def surviving_heroes(self):
        for hero in self.heroes:
            if hero.is_alive():
                print(hero.name)

    def kill_counter(self):
        tot = 0
        for hero in self.heroes:
            tot += hero.kills
        return tot

    def attack(self, other_team):
        running = True
        while running:
            team_1 = []
            team_2 = []
            for hero in self.heroes:
                if hero.is_alive():
                    team_1.append(hero)

            for hero in other_team.heroes:
                if hero.is_alive():
                    team_2.append(hero)

            if len(team_1) == 0:
                if len(team_2) == 0:
                    print("Its a DRAW!")
                    running = False

                elif len(team_2) > 0:
                    print(f"{other_team.name} has WON!")
                    running = False

            elif len(team_2) == 0:
                if len(team_1) == 0:
                    print("Its a DRAW!")
                    running = False

                elif len(team_1) > 0:
                    print(f"{self.name} has WON!")
                    running = False

            else:
                hero1 = random.choice(team_1)
                hero2 = random.choice(team_2)
                hero1.fight(hero2)

    def revive(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        # print("\n|| Team Statistics ||")

        kdr = 0
        tot_kills = 0
        tot_deaths = 0
        for hero in self.heroes:
            tot_kills += hero.kills
            tot_deaths += hero.deaths
        if tot_deaths == 0:
            kdr = tot_kills
        else:
            kdr = tot_kills/tot_deaths
        return kdr


class Arena:
    def __init__(self,):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team("Team 1")
        self.team_two = Team("Team 2")
        # create instance variables named team_one and team_two that
        # will hold our teams.

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        name = input("What will this hero be called?")
        hero = Hero(name)
        hero.add_ability(self.create_ability())
        hero.add_armor(self.create_armor())
        hero.add_weapon(self.create_weapon())
        return hero
        # This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What will your new ability be called?")
        max_dam = input("what should the max damage be for this ability?")
        return Ability(name, max_dam)

        # This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What will this weapon be called?")
        max_dam = input("What should the max damage be for this weapon?")
        return Weapon(name, max_dam)

        # This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("What will this armor be called?")
        max_blocked = input(
            "What should the max damage blocked be for this armor?")
        return Armor(name, max_blocked)

        # This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        hero_count = input(
            "Welcome! Let's start off by building team one! How many heros should be in team one? ")

        for index in range(0, int(hero_count)):
            self.team_one.add_hero(self.create_hero())
        pass
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        hero_count = input(
            "Now lets build team two! How many heroes should be in team two? ")
        for index in range(0, int(hero_count)):
            self.team_two.add_hero(self.create_hero())
        pass
        # This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print(f"Team One KD Ratio: {self.team_one.stats()}")
        print(f"Team Two KD Ratio: {self.team_two.stats()}")

        print("Surviving heroes: ")
        self.team_one.surviving_heroes()
        self.team_two.surviving_heroes()

        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive()
            arena.team_two.revive()
