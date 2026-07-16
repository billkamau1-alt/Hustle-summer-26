import random


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_damage= random.randint(0, self.max_block)
        print(random_damage)
        return random_damage


    def attack(self): # loops through a hero's abilities and totals up the damage from each attack
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage



    def add_armor(self): # adds an armor to a hero's list of armors
        self.armors.append(armor)

    
    def defend(self): # loops through a hero's armors and totals up the block from each armor
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block




    def take_damage(self, damage): #reduces the hero's health by ncoming damage, after subtracting what the amor can defend
        blocked = self.defend()
        actual_damage = max(damage - blocked, 0)
        self.current_health -= actual_damage
    if self.current_health <= 0:
        self.current_health = 0
    return actual_damage



if __name__ == "__main__":
    armor = Armor("Steel Shield", 30)
    # print(armor.name)
    # print(armor.max_block)
    # armor.block()
