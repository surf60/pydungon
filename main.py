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

        # Level up the player
        player.level += 1
        player.health += 1
        player.strength += 1
        player.agility += 1

        print(f"{player.name} has leveled up to level {player.level}!")
    elif not player.is_alive():
        print(f"{enemy.name} has defeated you!")

    # Ask the player if they want to fight again
    if player.is_alive():
        while True:
            response = input("Do you want to fight again? (yes/no): ")
            if response.lower() == "yes":
                # Create a new enemy and start the fight again
                enemy2 = EnemyCharacter("Goblin", 1, 5, 5, 3, 2)
                print(enemy2)
                fight(player, enemy2)
                break
            elif response.lower() == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


player1 = PlayerCharacter("John",1,15,3,1,1)
enemy1 = EnemyCharacter("Goblin", 1, 10, 5, 3, 2)

fight(player1,enemy1)
