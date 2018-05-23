import random
class Wizard:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def attack(self, creature):
        print('The Wizard {} attacks {}!'.format(
                self.name, creature.name))

        my_roll = random.randint(1,12) * self.level
        creature_roll = random.randint(1,12) * creature.level

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature.name,creature_roll))

        if my_roll >= creature_roll:
            print('The Wizard has handily triumphed over {}'. format(creature.name))
            return True
        else:
            print('The Wizard has been DEFEATED!!!')
            return False









class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level


    def __repr__(self):
        return 'Creature: {} of level {}'.format(self.name,self.level)
 





