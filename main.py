class Player:
    def __init__(self, health=200, energy=100): # constructor
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1):
        target.health -= damage 
        self.energy -= damage #self.energy = self.energy - damage
        if target.is_attacked():
            self.health -= target.damage
        print(f"attacking to monster, monster health : {target.health} left, your energy is {self.energy} left" )

class Monster:
    def __init__(self, health = 100, ):
        self.health = health # dinamis
        self.health_init = self.health # always 500
    
    def is_attacked(self):
        return self.health < self.health_init
        


player1 = Player()
player2 = Player()
oni = Monster(health=500)

player1.attack(target=oni, damage=80)
player2.attack(target=oni, damage=40)

oni.attack()





