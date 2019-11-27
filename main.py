import tkinter
from classes import *
from vis import *
from files_treatment import *



flag_perform = False
'''Флаг основногой цикличности'''
level_time = 0
'''Время уровня'''
time_step = 100
window = None
menu_level_botton = []
menu_record_button = None
exit_button = None
Name = None
list_levels = [
    'Level 1'
]
scores_file = 'High_score.txt'
level_objects = []
size_level = 0
hero = None



def execution():
    global flag_perform
    global time_step
    global exit_button
    global hero
    global level_objects
    global size_level
    global coords_win

    if flag_perform:
        window.after(time_step - int(time_speed.get()), execution)



def start_level(level_name):
    global level_objects
    global hero
    global size_level
    global coords_win
    level_objects = read_level(level_name, hero)
    size_level = count_size_level(level_objects)
    change_position(hero, size_level)




def main():
    global flag_perforn
    global level_time
    global time_step
    global window
    global menu_level_botton
    global menu_record_button
    global exit_button
    global Name

    root = tkinter.Tk()
    window = tkinter.Canvas(root, width = window_width, height = window_height, bg = 'black')
    window.pack(side = tkinter.BOTTOM)

    Name = tkinter.Label(window, textvariable = 'The Nario')
    Name.pack(side = tkinter.TOP)

    menu_record_button = tkinter.Button(window, textvariable = 'View the high score table', command = view_scores)
    menu_record_button.pack(side = tkinter.TOP)

    for level in list_levels:
        level_button = tkinter.Button(window, textvariable = level, command = start_level(level))
        menu_level_botton.append(level_button)
        level_button.pack(side = tkinter.HORIZONTAL)
        del level_button