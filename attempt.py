
monsters = []
towers = []

class Monster:
    def __init__(self, health, damage, currentTower):
        self.health = health
        self.damage = damage
        self.currentTower = currentTower

    def update(self):
        if self.currentTower is not None:
            self.currentTower.dealDamage(self)
            self.currentTower = self.currentTower.nextTower

class Tower:
    def __init__(self, health, regen, nextTower):
        self.health = health
        self.regen = regen
        self.nextTower = nextTower

    def dealDamage(self, monster):
        damage = min(monster.health, self.health)
        monster.health -= damage
        self.health -= damage


def update():
    for monster in monsters:
        monster.update()


