class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def showInfo(self):
        print("{} \n\thp: {}".format(self.name, self.hp))


class Hero_int(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    def showInfo(self):
        print("{} \n\tRole: INT\n\thp: {}".format(
            self.name, self.hp))  # override


class Hero_str(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


boxing = Hero_int("boxing")
tank = Hero_str("tank")

boxing.showInfo()
tank.showInfo()
