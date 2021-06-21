class Hero:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Hero_Intelligent(Hero):
    pass


priest = Hero("priest", 200)
wizard = Hero_Intelligent("wizard", 100)

print(priest.name)
print(help(wizard))
