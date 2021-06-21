class Hero:

    def __init__(self, inputName, inputHP, inputPower, inputDefense):
        self.name = inputName
        self.hp = inputHP
        self.power = inputPower
        self.defense = inputDefense

    def attack(self, opponent):
        print(self.name + " attack " + opponent.name)
        opponent.attacked(self, self.power)

    def attacked(self, opponent, damage):
        print(self.name + " attacked by " + opponent.name)
        damage_dealt = damage/self.defense
        print("Damage dealt : " + str(damage_dealt))
        self.hp -= damage_dealt
        print("HP " + self.name + ": " + str(self.hp))


sniper = Hero("sniper", 100, 10, 5)
assasin = Hero("assasin", 80, 20, 2)

sniper.attack(assasin)
print("=======")
assasin.attack(sniper)
