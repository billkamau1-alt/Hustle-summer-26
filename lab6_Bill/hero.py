from ability import Ability
from armor import Armor
import random


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health


    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        print(random.choice(my_list))



if __name__=="__main__":
    my_hero = Hero("spider-Man",150)
    print(my_hero.name)
    print(my_hero.current_health)
    my_opponent = Hero("Batman", 200)
    my_hero.battle(my_opponent)