
import random

# Soldier

class Soldier:
     def __init__(self, health, strength):
         self.health = health
         self.strength = strength

     def attack(self):
         return self.strength

     def receiveDamage(self, damage):
         self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
         super().receiveDamage
         self.health -= damage
         if self.health > 0:
             return f"{self.name} has received {damage} points of damage"
         else: 
             return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
         super().receiveDamage
         if self.health > 0:
             return f"A Saxon has received {damage} points of damage"
         else: 
             return "A Saxon has died in combat"


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        saxon_random = random.random(self.saxonArmy)
        vikatt = sax.receiveDamage(vik.strength)
        if Saxon.health <= 0:
            self.saxonArmy.remove(self.Saxon)

    def saxonAttack(self):
        viking_random = random.random(self.vikingArmy)
        saxatt = vik.receiveDamage(sax.strength)
        if Viking.health <= 0:
            self.vikingArmy.remove(self.Viking)


    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle"


