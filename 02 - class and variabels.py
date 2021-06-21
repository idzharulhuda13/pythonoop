class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHP, inputPower, inputDefense):
        # variabels
        self.name = inputName
        self.defense = inputDefense
        self.hp = inputHP
        self.power = inputPower
        Hero.jumlah += 1
        print("Hero " + inputName + " Created")


hero1 = Hero("huda", 100, 50, 200)
print(Hero.jumlah)
hero2 = Hero("idzharul", 200, 30, 100)
print(Hero.jumlah)
