class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def showInfo(self):
        print("{} dengan hp: {}".format(self.name, self.hp))


# class Hero_int:
class Hero_int(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showInfo()

# class Hero_str:


class Hero_str(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()


jaka = Hero_int('jaka')
ass = Hero_str('ass')

# print(jaka.name, " ", jaka.hp)
# print(ass.name, " ", ass.hp)
