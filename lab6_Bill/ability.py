class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        random_damage= random.randint(0, self.max_damage)
        print(random_damage)
        return random_damage


if __name__ =="__main__":
     ability = Ability("Fireball", 50)
     print(ability.name)
     print(ability.max_damage)
     ability_ .attack()
     my_ability.attack()