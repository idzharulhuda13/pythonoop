class Hero:
    pass


hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "Sniper"
hero1.health = 100

hero2.name = "Paladin"
hero2.health = 100

hero3.name = "Assasin"
hero3.health = 100

print(hero1)
print(hero1.__dict__)
print(hero1.name)
