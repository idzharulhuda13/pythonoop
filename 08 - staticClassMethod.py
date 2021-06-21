class Hero:
    # private class variabel
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # method ini hanya berlaku untuk class
    def getJumlahClass():
        return Hero.__jumlah

    # method static berlaku untuk keduanya
    @staticmethod
    def getJumlahAll():
        return Hero.__jumlah

    # class method berlaku untuk keduanya (polymorphism)
    @classmethod
    def getJumlahClass2(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(sniper.getJumlah())
hunter = Hero("hunter")
print(Hero.getJumlahClass())
clint = Hero("clint")
print(clint.getJumlahAll())
print(Hero.getJumlahAll())

print(Hero.getJumlahClass2())
print(hunter.getJumlahClass2())
