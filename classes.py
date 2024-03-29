class Block:
    type = None

    x = 0

    y = 0

    vx = 0

    vy = 0

    r = 0

    damage = 0

    image = None

    im = None

    imagetk = None

    color = 'green'

    movetime = 0

    nowtime = 0

    def parse_parametrs(self, line):
        self.x = float(line.split()[1])
        self.y = float(line.split()[2])
        self.vx = float(line.split()[3])
        self.vy = float(line.split()[4])
        self.r = float(line.split()[5])
        self.movetime = float(line.split()[6])
        self.damage = float(line.split()[6])
        self.type = line.split()[7].lower()
        self.image = line.split()[8].lower()
        if (self.vx != 0 or self.vy != 0):
            self.movetime = float(line.split()[9])
            self.nowtime = float(line.split()[10])


class Body:
    type = None

    x = 0

    y = 0

    vx = 0

    vy = 0

    r = 0

    image = None

    im = None

    imagetk = None

    life = 10

    status = None

    type_attack = None

    damage = 0

    loyalty = 0

    exp_reward = 0

    gold_reward = 0

    color = 'red'

    def parse_parametrs(self, line):
        self.x = float(line.split()[1])
        self.y = float(line.split()[2])
        self.vx = float(line.split()[3])
        self.vy = float(line.split()[4])
        self.r = float(line.split()[5])
        self.type = line.split()[6].lower()
        self.life = float(line.split()[7])
        self.type_attack = line.split()[8].lower()
        self.damage = float(line.split()[9])
        self.loyalty = int(line.split()[10])
        self.exp_reward = int(line.split()[11])
        self.gold_reward = int(line.split()[12])
        self.image = line.split()[13].lower()


class Item:
    type = None

    type_attack = None

    color = 'yellow'

    damage = 0

    cost = 0

    def parse_parametrs(self, line):
        self.type = line.split()[1].lower()
        self.type_attack = line.split()[2].lower()
        self.damage = float(line.split()[3])
        self.cost = int(line.split()[4])
        self.color = line.split()[5].lower()


def count_size_level(objects):
    size_variable = 100
    for obj in objects:
        if obj.x > size_variable:
            size_variable = obj.x + obj.r*3

    return size_variable
