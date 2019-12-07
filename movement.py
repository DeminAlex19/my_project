def move(obj, time_step):
    obj.x += obj.vx
    obj.y += obj.vy


def accel(obj, time_step, level_objects):
    obj.vx = 0
    obj.vy = 0
    '''if checkground(obj, level_objects) == False and type(obj).__name__ == 'Body':
        obj.vy += 0.01'''


def checkground(hero, level_objects):
    flag = False
    for obj in level_objects:
        if obj.type == 'ground':
            if (hero.x + hero.r >= obj.x - obj.r >= hero.x - hero.r or hero.x + hero.r >= obj.x + obj.r >= hero.x - hero.r or hero.x + hero.r <= obj.x + obj.r and hero.x - hero.r >= obj.x - obj.r) and (hero.y + hero.r == obj.y - obj.r):
                return True
                flag = True
    if flag == False:
        return False


def check_hit(body, obj, level_objects):
    if (body.x + body.r > obj.x + obj.r > body.x - body.r or body.x + body.r > obj.x - obj.r > body.x - body.r or body.x + body.r <= obj.x + obj.r and body.x - body.r >= obj.x - obj.r) and (body.y + body.r > obj.y + obj.r > body.y - body.r or body.y + body.r > obj.y - obj.r > body.y - body.r or body.y + body.r <= obj.y + obj.r and body.y - body.r >= obj.y - obj.r):
        if body.vx - obj.vx >= 0:
            if body.vy - obj.vy >= 0:
                if (body.x + body.r - obj.x + obj.r)*(body.vy - obj.vy) >= (body.y + body.r - obj.y + obj.r)*(body.vx - obj.vx):
                    if type(body).__name__ == 'Body':
                        body.vy = obj.vy
                        body.y = obj.y - obj.r - body.r
                    else:
                        obj.vy = body.vy
                        obj.y = body.y - body.r - obj.r


def action(body):
    if body.type_attack == 'sword':
        None
    elif body.type_attack == 'pistol':
        None


def special(body):
    None
