class Hero:
    def __init__(self, name, hp, power):
        self.__name = name
        self.__hp = hp
        self.__power = power

    # getter
    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    # setter
    def attacked(self, damage):
        self.__hp -= damage

    def powBonus(self, bonus):
        self.__power += bonus


assasin = Hero("assasin", 100, 20)

print(assasin.getName())
assasin.attacked(10)
print(assasin.getHp())
