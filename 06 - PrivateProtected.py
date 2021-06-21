class Hero:

    # class variabel
    jumlah = 0

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

        # variabel instance private
        self.__private = "private"

        # varibel instance protected
        self._protected = "protected"


huda = Hero("huda", 100)

print(huda.__dict__)
