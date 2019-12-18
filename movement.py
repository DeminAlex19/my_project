def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def move(level_objects, hero):
    for obj in level_objects:
        accel(obj, level_objects)
        obj.x += obj.vx
        obj.y += obj.vy
    for i in range(len(level_objects)):
        for j in range(i+1, len(level_objects)):
            if check_collusion(level_objects[i], level_objects[j]):
                collusion(level_objects[i], level_objects[j])
    hero.vx = 0


def accel(obj, level_objects):
    if type(obj).__name__ == 'Body':
        if not checkground(obj, level_objects) and type(obj).__name__ == 'Body':
            obj.vy += 0.05
        if checkground(obj, level_objects):
            if obj.vy > 0:
                obj.vy = 0
    if type(obj).__name__ == 'Block' and (obj.vx != 0 or obj.vy != 0):
        obj.nowtime += 1
        if obj.nowtime == obj.movetime:
            obj.vx *= -1
            obj.vy *= -1
            obj.nowtime = 0


def checkground(hero, level_objects):
    for obj in level_objects:
        if obj.type == 'ground':
            if (hero.x + hero.r > obj.x - obj.r > hero.x - hero.r or hero.x + hero.r > obj.x + obj.r > hero.x - hero.r or hero.x + hero.r <= obj.x + obj.r and hero.x - hero.r >= obj.x - obj.r) and (hero.y + hero.r <= obj.y - obj.r <= hero.y + hero.r):
                hero.y = obj.y - hero.r - obj.r
                hero.vx += obj.vx
                return True
        elif obj.type == 'exit':
            if (hero.x + hero.r >= obj.x - obj.r >= hero.x - hero.r or hero.x + hero.r >= obj.x + obj.r >= hero.x - hero.r or hero.x + hero.r <= obj.x + obj.r and hero.x - hero.r >= obj.x - obj.r) and (hero.y + hero.r >= obj.y - obj.r >= hero.y - hero.r or hero.y + hero.r >= obj.y + obj.r >= hero.y - hero.r or hero.y + hero.r <= obj.y + obj.r and hero.y - hero.r >= obj.y - obj.r):
                hero.status = 'level end'
                return False
    return False


def check_collusion(obj1, obj2):
    if type(obj1).__name__ != 'Body' and type(obj2).__name__ != 'Body':
        return False
    if (obj1.x - obj2.x) * sign(obj1.x - obj2.x + 0.0001) < obj1.r + obj2.r and\
            (obj1.y - obj2.y) * sign(obj1.y - obj2.y + 0.0001) < obj1.r + obj2.r:
        return True
    return False


def collusion(obj1, obj2):
    if type(obj2).__name__ == 'Body':
        collusion(obj2, obj1)
    else:
        dx = obj1.r + obj2.r - (obj1.x - obj2.x) * sign(obj1.x - obj2.x)
        dy = obj1.r + obj2.r - (obj1.y - obj2.y) * sign(obj1.y - obj2.y)
        if (obj1.vx - obj2.vx) == 0:
            tx = 10000000
        else:
            tx = dx / (obj1.vx - obj2.vx)
            tx *= sign(tx)
        if (obj1.vy - obj2.vy) == 0:
            ty = 10000000
        else:
            ty = dy / (obj1.vy - obj2.vy)
            ty *= sign(ty)
        if tx < ty:
            if (obj1.x <= obj2.x - sign(obj1.vx - obj2.vx + 0.00000001) * (
                        obj1.r + obj2.r) <= obj1.x - obj1.vx or obj1.x - obj1.vx <= obj2.x - sign(obj1.vx - obj2.vx + 0.00000001)*(obj1.r + obj2.r) <= obj1.x):
                obj1.x = obj2.x - sign(obj1.vx - obj2.vx + 0.00000001)*(obj1.r + obj2.r)
            else:
                obj1.x = obj2.x + sign(obj1.vx - obj2.vx + 0.00000001)*(obj1.r + obj2.r)
            obj1.vx = obj2.vx
        elif ty < tx:
            if (obj1.y <= obj2.y - sign(obj1.vy - obj2.vy + 0.00000001)*(obj1.r + obj2.r) <= obj1.y - obj1.vy or \
                    obj1.y - obj1.vy <= obj2.y - sign(obj1.vy - obj2.vy + 0.00000001)*(obj1.r + obj2.r) <= obj1.y):
                obj1.y = obj2.y - sign(obj1.vy - obj2.vy + 0.00000001)*(obj1.r + obj2.r)
            else:
                obj1.y = obj2.y + sign(obj1.vy - obj2.vy + 0.00000001)*(obj1.r + obj2.r)
            obj1.vy = obj2.vy


def action(body):
    if body.type_attack == 'sword':
        None
    elif body.type_attack == 'pistol':
        None


def special(body):
    None
