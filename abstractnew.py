from abc import ABC, abstractmethod

# Abstract Base Class for Weapons
class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass


# Concrete Weapon Classes
class Sword(Weapon):
    def attack(self):
        print("Cuts and stabs")


class Bow(Weapon):
    def attack(self):
        print("Shoots arrows")


# Fighter Class
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon  # Assigns an instance of a weapon class

    def change_weapon(self):
        if isinstance(self.weapon, Sword):  # Check if the current weapon is a Sword
            self.weapon = Bow()  # Change to Bow
        else:
            self.weapon = Sword()  # Change to Sword

    def attack(self):
        print(f"{self.name} attacks with their weapon:")
        self.weapon.attack()


# Example Usage
f1 = Fighter("Arny", Sword())  # Start with a Sword
f1.attack()  # Should print "Cuts and stabs"

f1.change_weapon()  # Switch to Bow
f1.attack()  # Should print "Shoots arrows"

f1.change_weapon()  # Switch back to Sword
f1.attack()  # Should print "Cuts and stabs"
