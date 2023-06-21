class Player:
    def __init__(self, health, energy=100): # constructor
        self.health = health
        self.energy = energy
        print(f"player created")

    def attack(self, damage = 1):
        self.target = monster.health
        self.energy -= damage #self.energy = self.energy - damage
        print("attacking!!!")

class Monster:
    def __init__(self, health = 100, ):
        self.health = health
        print("monster created")



player = Player(health=200)
monster = Monster(health=500)

player.attack(damage=80,)



