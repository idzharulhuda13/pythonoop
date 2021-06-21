class Hero:

    def __init__(self, name, hp, defense):
        self.name = name
        self.__hp = hp
        self.__defense = defense

    @property
    def info(self):
        return "name {} : \n\tHp: {} \n\tDefense: {}".format(self.name, self.__hp, self.__defense)

    @property
    def defense(self):
        pass

    @defense.getter
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, bonus):
        self.__defense += bonus

    @defense.deleter
    def defense(self):
        print("defense di netralkan")
        self.__defense = None


sniper = Hero("sniper", 100, 20)

print(sniper.info)
sniper.name = "hunter"
print(sniper.info)

print("getter dan setter untuk __defense:")
print(sniper.defense)
sniper.defense = 20
print(sniper.defense)
del sniper.defense
print(sniper.defense)
