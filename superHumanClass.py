class Human(object):
    def __init__(self, name, health, intelligence, stealth, strength):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.stealth = stealth
        self.strength = strength
    def stats(self):
        print ("The {} Name: {}, Health: {}, Intelligence: {}, Stealth: {}, Strength: {}".format( self.__class__.__name__ , self.name, self.health, self.intelligence, self.stealth, self.strength))

class Wizard(Human):
    def __init__(self,name, health, intelligence, stealth, strength):
        super(Wizard, self ).__init__(name, health, intelligence, stealth, strength)   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
        print("The Wizard " + self.name + " gained 10 health points.")
        
class Ninja(Human):
    def __init__(self,name, health, intelligence, stealth, strength):
        super(Ninja, self).__init__(name, health, intelligence, stealth, strength)    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
        print("The ninja " + self.name + " gained 5 stealth points.")
        
class Samurai(Human):
    def __init__(self,name, health, intelligence, stealth, strength):
        super(Samurai, self).__init__(name, health, intelligence, stealth, strength)  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
        print("The Samurai " + self.name + " secrificed his body and lost 5 health")

human = Human("jerry", 10, 10, 5, 5)
human.stats()
wizard = Wizard("gandalf", 5, 20, 2, 2)
wizard.heal()
wizard.stats()
ninja = Ninja("naruto",20,10,30,10)
ninja.steal()
ninja.stats()
samurai = Samurai("afro",10,10,10,20)
samurai.sacrifice()

