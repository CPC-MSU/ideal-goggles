
monsters = []
towers = []

class Monster:
    def __init__(self, spawnTime, health):
        self.health = health
        self.spawnTime = spawnTime

    def update(self, time):
        if time < self.spawnTime:
            return True
        else:
            towerNumber = time - self.spawnTime
            if towerNumber >= len(towers):
                return False
            else:
                currentTower = towers[towerNumber]
                currentTower.dealDamage(self)
                return True

    def __str__(self):
        return "monster: " + str(self.health) + ", " + str(self.spawnTime)
            

class Tower:
    def __init__(self, capacity, regen):
        self.health = capacity
        self.capacity = capacity
        self.regen = regen

    def dealDamage(self, monster):
        damage = min(monster.health, self.health)
        monster.health -= damage
        self.health -= damage

    def update(self):
        self.health = min(self.health + self.regen, self.capacity)

    def __str__(self):
        return "tower: " + str(self.health) + ", " + str(self.regen)


def update(time):
    completeState = False
    completeState = [monster.update(time) for monster in monsters]
    
    for tower in towers:
        tower.update()
    
    gameComplete = True not in completeState

    if gameComplete:
        end = sum([monster.health for monster in monsters])
        print(end)
        return False
    return True


singles = 0

fileName = input("Please enter the name of the .txt file to read: ")

try:
    file = open(fileName, "r")
except:
    file = open(fileName + ".txt", "r")
for l, line in enumerate(file):
    lineList = line.split()
    lineSize = len(lineList)
    if lineSize == 1:
        singles += 1
    elif lineSize == 2:
        if singles == 1:
            towers.append(Tower(int(lineList[0]), int(lineList[1])))

        if singles == 2:
            monsters.append(Monster(int(lineList[0]), int(lineList[1])))
            
            

cont = True
time = 0

while cont:
    cont = update(time)
    time += 1

