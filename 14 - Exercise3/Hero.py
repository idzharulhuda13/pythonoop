class Hero:
    def __init__(self, name):
        self.hp_pool = [0, 100, 200, 300, 400, 500]
        self.pow_pool = [0, 10, 20, 30, 40, 50]
        self.def_pool = [0, 1, 2, 3, 4, 5]
        self.__name = name
        self.__exp = 0
        self.__lvl = 0

    def show_info(self):
        print("{} \n\tlevel: {}\n\thp: {}\n\tpower: {}\n\tdefense: {}".format(
            self.__name, self.__lvl, self.__hp, self.__pow, self.__def))

    @property
    def hp_pool(self):
        pass

    @property
    def pow_pool(self):
        pass

    @property
    def def_pool(self):
        pass

    @property
    def lvlUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @hp_pool.setter
    def hp_pool(self, input):
        self.__hp_pool = input

    @pow_pool.setter
    def pow_pool(self, input):
        self.__pow_pool = input

    @def_pool.setter
    def def_pool(self, input):
        self.__def_pool = input

    @lvlUp.setter
    def lvlUp(self, input):
        self.__lvl += input
        self.__hp = self.__hp_pool[self.__lvl]
        self.__pow = self.__pow_pool[self.__lvl]
        self.__def = self.__def_pool[self.__lvl]

    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if(self.__exp >= 100):
            self.lvlUp = self.__exp//100
            self.__exp %= 100


class HeroInt(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hp_pool = [0, 50, 100, 150, 200, 250]
        self.pow_pool = [0, 20, 40, 60, 80, 100]
        self.def_pool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.lvlUp = 1


class HeroStr(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hp_pool = [0, 200, 400, 600, 800, 1000]
        self.pow_pool = [0, 20, 40, 60, 80, 100]
        self.def_pool = [1, 2, 3, 4, 6, 10]
        self.lvlUp = 1
