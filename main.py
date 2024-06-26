import random

class PlayerCharacter:
    def __init__(self, name="Default", level=1, health=100, strength=10, agility=5, intelligence=2):
        self.level = level
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if self.is_alive():
            self.health -= damage
            print(f"{self.name} took {damage} points of damage. Health remaining: {self.health}")
            if not self.is_alive():
                print(f"{self.name} has died!")
        else:
            print(f"{self.name} has died!")

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, Health: {self.health}, Strength: {self.strength}, Agility: {self.agility}, Intelligence: {self.intelligence}"
    
class EnemyCharacter:
    def __init__(self, name="Default", level=1, health=100, strength=10, agility=5, intelligence=2):
        self.level = level
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def is_alive(self): 
        return self.health > 0 

    def take_damage(self, damage): 
        if self.is_alive(): 
            self.health -= damage 
            print(f"{self.name} took {damage} points of damage. Health remaining: {self.health}") 
            if not self.is_alive(): 
                print(f"{self.name} has died!") 
        else: 
            print(f"{self.name} has died!") 

    def __str__(self): 
        return f"Name: {self.name}, Level: {self.level}, Health: {self.health}, Strength: {self.strength}, Agility: {self.agility}, Intelligence: {self.intelligence}"
    
def level_up(player):
    player.level += 1
    player.health += random.randint(3,7)
    player.strength += random.randint(1,3)
    player.agility += random.randint(1,3)
    print(f"{player.name} has leveled up to level {player.level}!")

def loot_drop(boost_map, player):
    item_to_drop = random.choice(list(boost_map.keys()))
    stat_boost = boost_map.get(item_to_drop, "None")

    if stat_boost:
        if stat_boost == "health":
            player.health += 10
        elif stat_boost == "strength":
            player.strength += 1
        elif stat_boost == "agility":
            player.agility += 1

        print(f"You found a {item_to_drop} and gained +{stat_boost}!")

def death(player):
    print(f"{player.name} is now Dead")
    
def fight(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player_attacks = random.randint(player.strength - 3, player.strength)
        print(f"{player.name} attacks {enemy.name} for {player_attacks} damage!")
        enemy.take_damage(player_attacks)

        if not enemy.is_alive():
            break

        enemy_attacks = random.randint(enemy.strength - 3, enemy.strength)
        print(f"{enemy.name} attacks {player.name} for {enemy_attacks} damage!")
        player.take_damage(enemy_attacks)

    if player.is_alive() and not enemy.is_alive():
        print("Congratulations, you have won the fight!")
        level_up(player)
    elif not player.is_alive():
        print(f"{enemy.name} has defeated you!")
        death(player)

    if player.is_alive() and not enemy.is_alive():
        print("Congratulations, you have won the fight!")
        level_up(player)

    elif not player.is_alive():
        print(f"{enemy.name} has defeated you!")
        death(player)

def create_enemy(player_level):
    base_health = 10
    health_diff = random.randint(-2, 3)
    enemy_health = base_health + (player_level - 1) + health_diff

    base_strength = 5
    strength_diff = random.randint(-1, 2)
    enemy_strength = base_strength + (player_level - 1) + strength_diff

    return EnemyCharacter(f"Level {player_level} Enemy", player_level, enemy_health, enemy_strength, 3, 2)

player1 = PlayerCharacter("John",1,15,3,1,1)
#enemy1 = EnemyCharacter("Goblin", 1, 10, 5, 3, 2)
enemy1 = create_enemy(player1.level)

level_up(player1)
items = {"Health Potion": "health", "Strength Tonic": "strength", "Agility Elixir": "agility"}
loot_drop(items, player1)
fight(player1,enemy1)
while player1.is_alive():  # While the player is alive
    enemy1 = create_enemy(player1.level)  # Create an enemy of the same level as the player
    print(enemy1)
    fight(player1, enemy1)  # Fight the enemy
    print(player1)
    input('Continue: ')  # Wait for user to continue
