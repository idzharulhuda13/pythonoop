class Hero:
    # private class variabel
    __jumlah = 0

    def __init__(self, name, hp, power, defense):
        self.__name = name
        self.__baseHp = hp
        self.__baserPower = power
        self.__baseDefense = defense
        self.__level = 1
        self.__exp = 0

        self.__maxHp = self.__baseHp * self.__level
        self.__power = self.__baserPower * self.__level
        self.__defense = self.__baseDefense * self.__level

        self.__hp = self.__maxHp

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thp = {}/{} \n\tpower = {} \n\tdefense = {}".format(self.__name, self.__level, self.__hp, self.__maxHp, self.__power, self.__defense)

    @property
    def gainExp(self):
        pass

    def getName(self):
        return self.__name

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name + " level up")
            self.__level += 1
            self.__exp -= 100

            self.__maxHp = self.__baseHp * self.__level
            self.__power = self.__baserPower * self.__level
            self.__defense = self.__baseDefense * self.__level

    def attack(self, opponent):
        print("{} attack {}, get 50 experience".format(
            self.__name, opponent.getName()))
        self.gainExp = 50


hunter = Hero("hunter", 100, 30, 8)
priest = Hero("priest", 100, 30, 8)

print(hunter.info)

hunter.attack(priest)
hunter.attack(priest)

print(hunter.info)
print(priest.info)
print(hunter.__dict__)
