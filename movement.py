def move(obj, time_step):
    obj.x += obj.vx
    obj.y += obj.vy


def accel(obj, time_step, level_objects):
    obj.vx = 0
    if checkground(obj, level_objects) == False:
        obj.y += 0.05


def checkground(hero, level_objects):
    flag = False
    for obj in level_objects:
        if obj.type == 'ground':
            if hero.x + hero.r >= obj.x - obj.r >= hero.x - hero.r or hero.x + hero.r >= obj.x + obj.r and hero.x - hero.r <= obj.x + obj.r:
                return True
                flag = True
    if flag == False:
        return False


def check_hit(body, obj):
    None


def action(body):
    if body.type_attack == 'sword':
        None
    elif body.type_attack == 'pistol':
        None


def special(body):
    None
