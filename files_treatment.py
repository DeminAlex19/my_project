from classes import *
import datetime

def read_level(level_name, hero_obj):
    objects = []

    with open(level_name + '.txt') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            object_type = line.split()[0].lower()
            if(object_type == "block"):
                block_one = Block()
                block_one.parse_parameters(line)
                objects.append(block_one)
                del block_one
            if(object_type == "body"):
                body_one = Body()
                body_one.parse_parametrs(line)
                objects.append(body_one)
                if(body_one.type.lower() == 'hero'):
                    hero_obj = body_one
                del body_one
            if(object_type == "item"):
                item_one = Item()
                item_one.parse_parametrs(line)
                objects.append(item_one)
                del item_one
            del object_type

    return objects


def write_scores(file, score):
    with open(file, 'w') as out_file:
        print(out_file, "%s %d" % (str(datetime.datetime.now()) , score))