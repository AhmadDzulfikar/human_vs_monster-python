class Player:
    def __init__(self, name, health=200, energy=100): # constructor
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1):
        target.health -= damage 
        self.energy -= damage #self.energy = self.energy - damage
        print(f"{self.name} attacking {damage} damage to {target.name}! ")
        if target.is_attacked(player_name=self.name):
            self.health -= target.damage

    def show_info(self):
        print(f"{self.name} health : {self.health}")
        print(f"{self.name} energy : {self.energy}")

class Monster:
    def __init__(self, name, health = 100, ):
        self.name = name
        self.health = health # dinamis
        self.health_init = self.health # always 500
        self.damage = 10
    
    def is_attacked(self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}")
        return self.health < self.health_init
    
    def show_info(self):
        print(f"{self.name} health : {self.health}")
        


player1 = Player(name="player1")
player2 = Player(name="player2")
onis = Monster(name="Oni", health=500)
reptiles = Monster(name="Reptile")

player1.attack(target=onis, damage=80)
player2.attack(target=reptiles, damage=40)

player1.show_info()
player2.show_info()

# oni.attack()cls





