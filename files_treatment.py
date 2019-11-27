from classes import *

def read_level(level_name):
    objects = []
    with open(level_name + '.txt') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue