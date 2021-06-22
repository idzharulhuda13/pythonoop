from Hero import HeroInt, HeroStr

mage = HeroInt("mage")
tank = HeroStr("tank")

mage.show_info()
tank.show_info()

mage.gainExp = 300
tank.gainExp = 250

mage.show_info()
tank.show_info()
