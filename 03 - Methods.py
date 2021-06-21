class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHP, inputPower, inputDefense):
        self.name = inputName
        self.hp = inputHP
        self.power = inputPower
        self.defense = inputDefense
        Hero.jumlah_hero += 1

    # void function, method without return
    def whoami(self):
        print("i am " + self.name)

    # method with argumetn
    def addHP(self, addHP):
        self.hp += addHP

    # method with return
    def getHP(self):
        return self.hp


hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("Assasin", 80, 20, 2)

hero1.whoami()
hero1.addHP(10)
print(hero1.getHP())

print(hero1.__dict__)
print(hero2.__dict__)
