class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)


class Role:
    def setRole(self, role):
        self.role = role

    def showRole(self):
        print(self.role)


class Hero(Team, Role):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


tank = Hero("tank", 200)
tank.setTeam("Red")
tank.setRole("str")

tank.showTeam()
tank.showRole()
