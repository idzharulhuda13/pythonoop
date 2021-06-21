class Hero:

    def __init__(self, inputName, inputHP, inputPower, inputDefense):
        self.name = inputName
        self.defense = inputDefense
        self.hp = inputHP
        self.power = inputPower


hero1 = Hero("huda", 100, 50, 200)
hero2 = Hero("idzharul", 200, 30, 100)

print(hero1.__dict__)
print(hero2.__dict__)
