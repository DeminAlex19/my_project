import tkinter
from classes import *
from vis import *
from tkinter.filedialog import *
from files_treatment import *



flag_perform = False
'''Флаг основногой цикличности'''
level_time = 0
'''Время уровня'''
time_step = 100
window = None
menu_level_button = []
menu_record_button = None
exit_button = None
Name = None

list_levels = [
    'Level 1'
]
scores_file = 'High_score.txt'
level_objects = []
size_level = 0
coords_win = [0, 0]
hero = None

screen_pause = None
continue_button = None



def execution():
    global flag_perform
    global time_step
    global exit_button
    global hero
    global level_objects
    global size_level
    global coords_win

    coords_win = change_position(hero, size_level, coords_win)
    if flag_perform:
        window.after(time_step, execution)



def start_level(level_name):
    global menu_level_button
    global menu_record_button
    global flag_perform
    global level_time
    global level_objects
    global hero
    global size_level
    global coords_win
    flag_perform = True
    level_time = 0
    for button in menu_level_button:
        window.delete(button)
    window.delete(menu_record_button)
    pause_button = tkinter.Button(window, text = 'Pause', command = stop_execution, width = 10)
    pause_button.pack(side = tkinter.TOP)
    level_objects = read_level(level_name, hero)
    size_level = count_size_level(level_objects)
    coords_win = change_position(hero, size_level, coords_win)

    execution()


def stop_execution():
    global screen_pause
    global flag_perform
    global continue_button
    flag_perform = False
    screen_pause = window.create_rectangle([0, 0], [window_width, window_height], fill = 'black')
    continue_button = tkinter.Button(window, text = 'Continue', command = continue_execution, width = 10)
    continue_button.pack(side = CENTER)


def continue_execution():
    global screen_pause
    global flag_perform
    global continue_button
    flag_perform = True
    window.delete(screen_pause)
    window.delete(continue_button)
    execution()



def main():
    global flag_perform
    global level_time
    global time_step
    global window
    global menu_level_button
    global menu_record_button
    global exit_button
    global Name

    root = tkinter.Tk()
    window = tkinter.Canvas(root, width = window_width, height = window_height, bg = 'black')
    window.pack(side = tkinter.BOTTOM)

    Name = tkinter.Label(window, textvariable = 'The Nario')
    Name.pack(side = tkinter.TOP)

    menu_record_button = tkinter.Button(window, text = 'View the high score table', command = view_scores)
    menu_record_button.pack(side = tkinter.TOP)

    for level in list_levels:
        level_button = tkinter.Button(window, text = level, command = start_level(level))
        menu_level_button.append(level_button)
        level_button.pack(side = tkinter.CENTER)
        del level_button