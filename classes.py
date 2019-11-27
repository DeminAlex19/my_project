class Block:
    type = None

    x = 0

    y = 0

    vx = 0

    vy = 0

    r = 0

    damage = 0

    image = None

    color = 'green'

    def parse_parametrs(self, line):
        self.x = int(line.split()[1])
        self.y = int(line.split()[2])
        self.r = int(line.split()[3])
        self.damage = int(line.split()[4])
        self.color = line.split()[5]


class Body:
    type = None

    x = 0

    y = 0

    vx = 0

    vy = 0

    r = 0

    image = None

    life = 10

    type_attack = None

    damage = 0

    loyalty = 0

    exp_reward = 0

    gold_reward = 0

    color = 'red'

    def parse_parametrs(self, line):
        self.x = int(line.split()[1])
        self.y = int(line.split()[2])
        self.vx = int(line.split()[3])
        self.vy = int(line.split()[4])
        self.r = int(line.split()[5])
        self.type = line.split()[6]
        self.life = int(line.split()[7])
        self.type_attack = line.split()[8]
        self.damage = int(line.split()[9])
        self.loyalty = int(line.split()[10])
        self.exp_reward = int(line.split()[11])
        self.gold_reward = int(line.split()[12])
        self.color = line.split()[13]


class Item:
    type_attack = None

    color = 'yellow'

    damage = 0

    cost = 0

    def parse_parametrs(self, line):
        self.type_attack = line.split()[1]
        self.damage = int(line.split()[2])
        self.cost = int(line.split()[3])
        self.color = line.split()[4]
