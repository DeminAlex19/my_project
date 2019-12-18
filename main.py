import tkinter
from classes import *
from vis import *
from tkinter.filedialog import *
from files_treatment import *
from movement import *

root = tkinter.Tk()
window_width = 1600
window_height = 800
root.geometry(str(window_width) + 'x' + str(window_height + 20))
window = None
frame = None

list_levels = ['Level 1', 'Level 2', 'Level 3']
level_objects = []
size_level = 0
coords_win = [0, 0]
hero = None
score = 0
level_name = ''
dead_scene = None
end_after = None

flag_perform = False
'''Флаг основногой цикличности'''
level_time = 0
'''Время уровня'''
time_step = 3
leb = None
score_options = []

menu_level_button = []
menu_record_button = None
pause_button = None
screen_pause = None
continue_button = None
exit_button = None

press_button_left = False  # 65
press_button_up = False  # 87
press_button_right = False  # 68
press_button_down = False  # 83
press_button_act = False  # 69
press_button_special = False  # 81


def view_scores():
    global leb
    if leb == None:
        with open('high scores.txt') as in_file:
            str = ''
            for line in in_file.readlines():
                str += line
            leb = tkinter.Label(window, text=str, width=100, bg='black', fg='white', font=('Arial 32', 10, 'bold'))
            leb.pack()


def checkPress(event):
    global press_button_left
    global press_button_up
    global press_button_right
    global press_button_down
    global press_button_act
    global press_button_special
    if event.keycode == 81:
        press_button_special = True
    if event.keycode == 87:
        press_button_up = True
    if event.keycode == 69:
        press_button_act = True
    if event.keycode == 65:
        press_button_left = True
    if event.keycode == 83:
        press_button_down = True
    if event.keycode == 68:
        press_button_right = True


def checkRelease(event):
    global press_button_left
    global press_button_up
    global press_button_right
    global press_button_down
    global press_button_act
    global press_button_special
    if event.keycode == 81:
        press_button_special = False
    if event.keycode == 87:
        press_button_up = False
    if event.keycode == 69:
        press_button_act = False
    if event.keycode == 65:
        press_button_left = False
    if event.keycode == 83:
        press_button_down = False
    if event.keycode == 68:
        press_button_right = False


def execution():
    global flag_perform
    global level_time
    global time_step
    global pause_button
    global continue_button
    global hero
    global level_objects
    global size_level
    global coords_win
    global press_button_left
    global press_button_up
    global press_button_right
    global press_button_down
    global press_button_act
    global press_button_special
    global score
    global score_options
    global dead_scene
    global end_after
    level_time += time_step/1000

    if press_button_right:
        hero.vx += 1
    if press_button_left:
        hero.vx += -1
    if press_button_up and checkground(hero, level_objects):
        hero.vy = -4
    if press_button_down:
        hero.typeattack = 'fall'
        hero.vy = 5
    if press_button_special:
        special(hero)
        press_button_special = False
    if press_button_act and press_button_special != True:
        action(hero)
        press_button_act = False
    if hero.status == 'level end':
        score = 50
        if level_time > score_options[0]:
            score -= int(level_time - score_options[0])*score_options[1]

        score -= (10 - hero.life)*10
        if score < 0:
            score = 0
        write_scores('high scores.txt', level_name, score)
        score = 0
        level_time = 0
        stop_execution()
        level_end()
    if hero.y >= window_height or hero.life <= 0:
        stop_execution()
        if continue_button != None:
            continue_button.destroy()
            continue_button = None
        if pause_button != None:
            pause_button.destroy()
            pause_button = None
        dead_scene = tkinter.Label(window, text='\n\nYou are died...', bg='black', fg='red', font=('Arial 64', 64, 'bold'))
        dead_scene.pack()
        end_after = root.after(3000, level_end)
    move(level_objects, hero)
    coords_win = change_position(hero, size_level, coords_win, window_width, window_height)
    for obj in level_objects:
        update_image(window, obj, coords_win)
    if flag_perform:
        window.after(time_step, execution)


def start_level(level):
    global leb
    global menu_level_button
    global menu_record_button
    global flag_perform
    global level_time
    global level_objects
    global hero
    global size_level
    global coords_win
    global frame
    global pause_button
    global exit_button
    global level_name
    global root
    global score_options
    if leb != None:
        leb.destroy()
        leb = None
    level_name = level
    flag_perform = True
    level_time = 0
    for button in menu_level_button:
        button.destroy()
    menu_record_button.destroy()
    pause_button = tkinter.Button(frame, text='Pause', command=stop_execution)
    pause_button.pack(side=tkinter.LEFT)
    exit_button = tkinter.Button(frame, text='Main menu', command=level_end)
    exit_button.pack(side=tkinter.RIGHT)
    level_objects = read_level(level)
    score_options = score_option(level)
    hero = find_hero(level_objects, hero)
    size_level = count_size_level(level_objects)
    coords_win = change_position(hero, size_level, coords_win, window_width, window_height)
    for obj in level_objects:
        create_image(window, obj, coords_win)

    root.bind('<KeyPress>', checkPress)
    root.bind('<KeyRelease>', checkRelease)
    execution()
    # удаление меню, создание уровня из файла, создание кнопки паузыб запуск выполнения


def stop_execution():
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global frame
    global window
    flag_perform = False
    pause_button.destroy()
    screen_pause = window.create_rectangle([0, 0], [window_width, window_height], fill='black')
    continue_button = tkinter.Button(frame, text='Continue', command=continue_execution, width=10)
    continue_button.pack(side=LEFT)
    # остановка выполнения и создание кнопки продолжения


def continue_execution():
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global frame
    global window
    flag_perform = True
    window.delete(screen_pause)
    continue_button.destroy()
    pause_button = tkinter.Button(frame, text='Pause', command=stop_execution)
    pause_button.pack(side=tkinter.LEFT)
    execution()
    # Удаление кнопки продолжения и запуск выполнения


def level_end():
    global screen_pause
    global level_objects
    global continue_button
    global score
    global exit_button
    global flag_perform
    global pause_button
    global level_name
    global dead_scene
    global end_after
    del end_after
    if dead_scene != None:
        dead_scene.destroy()
        dead_scene = None
    flag_perform = False
    level_name = ''
    score = 0
    if continue_button != None:
        continue_button.destroy()
    if pause_button != None:
        pause_button.destroy()
    exit_button.destroy()
    window.delete(screen_pause)
    screen_pause = None
    window.delete(ALL)
    menu()


def menu():
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    level_objects = []


    menu_record_button = tkinter.Button(window, text='View the high score table', command=view_scores)
    menu_record_button.pack(side=tkinter.TOP)

    level_button = tkinter.Button(window, text='Level 1', command=lambda: start_level('Level 1'))
    menu_level_button.append(level_button)
    level_button.pack()

    level_button = tkinter.Button(window, text='Level 2', command=lambda: start_level('Level 2'))
    menu_level_button.append(level_button)
    level_button.pack()

    level_button = tkinter.Button(window, text='Level 3', command=lambda: start_level('Level 3'))
    menu_level_button.append(level_button)
    level_button.pack()

    del level_button


def main():
    global time_step
    global window
    global menu_level_button
    global menu_record_button
    global pause_button
    global continue_button
    global frame

    frame = tkinter.Frame(root)
    frame.pack(side=TOP)
    name = tkinter.Label(frame, text="The Nario", width=10, bg='yellow', fg='red', font=('Arial 32', 10, 'bold'))
    name.pack(side=RIGHT)
    window = tkinter.Canvas(root, bg='cyan')
    window.pack(fill=BOTH, expand=1)

    menu()
    root.mainloop()


main()
