from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod

    def attack(self):
        pass

 class Sword(Weapon):
     def attack(self):
         print("cuts and stabs")

class Bow(Weapon):
    def attack(self):
        print("shoots arrows")

class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon



   #def change_weapon (self):
        if self.weapon == Sword:
            self.weapon = Bow()
        else: self.weapon = Sword()#


    def change_weapon(self):
        if isinstance(self.weapon, Sword):
            self.weapon = Bow()
        else:
            self.weapon= Sword



    def attack(self):
        print(f"{self.name}attacks with his weapon")
        self.weapon.attack()

f1 = Fighter("Arny",Sword())

f1.attack()
f1.change_weapon()
f1.attack()




