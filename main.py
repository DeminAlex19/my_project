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

list_levels = [
    'Level 1'
]
level_objects = []
size_level = 0
coords_win = [0, 0]
hero = None

flag_perform = False
'''Флаг основногой цикличности'''
level_time = 0
'''Время уровня'''
time_step = 1

menu_level_button = []
menu_record_button = None
pause_button = None
screen_pause = None
continue_button = None

press_button_left = False  # 65
press_button_up = False  # 87
press_button_right = False  # 68
press_button_down = False  # 83
press_button_act = False  # 69
press_button_special = False  # 81


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
    level_time += time_step
    if press_button_right:
        hero.vx = 0.5
    if press_button_left:
        hero.vx = -0.5
    if press_button_up:#and checkground(hero, level_objects)
        hero.vy -= 0.5
    if press_button_down:
        hero.typeattack = 'fall'
        hero.vy += 0.5
    if press_button_special:
        special(hero)
        press_button_special = False
    if press_button_act and press_button_special != True:
        action(hero)
        press_button_act = False
    for body in level_objects:
        move(body, time_step)
        for obj in level_objects:
            if obj != body:
                check_hit(body, obj, level_objects)
        accel(body, time_step, level_objects)
    coords_win = change_position(hero, size_level, coords_win, window_width, window_height)
    for obj in level_objects:
        update_image(window, obj, coords_win)

    print(hero.x, hero.y, hero.vx, hero.vy)
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
    global frame
    global pause_button
    flag_perform = True
    level_time = 0
    for button in menu_level_button:
        button.destroy()
    menu_record_button.destroy()
    pause_button = tkinter.Button(frame, text='Pause', command=stop_execution)
    pause_button.pack(side=tkinter.LEFT)
    level_objects = read_level(level_name)
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


def menu():
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    level_objects = []
    window = tkinter.Canvas(root, bg='blue')
    window.pack(fill=BOTH, expand=1)
    menu_record_button = tkinter.Button(window, text='View the high score table', command=view_scores)
    menu_record_button.pack(side=tkinter.TOP)

    for level in list_levels:
        level_button = tkinter.Button(window, text=level, command=lambda: start_level(level))
        menu_level_button.append(level_button)
        level_button.pack()
        del level_button


def main():
    global time_step
    global window
    global menu_level_button
    global menu_record_button
    global pause_button
    global frame

    frame = tkinter.Frame(root)
    frame.pack(side=TOP)
    name = tkinter.Label(frame, text="The Nario", width=10, bg='yellow', fg='red', font=('Arial 32', 10, 'bold'))
    name.pack(side=RIGHT)

    menu()
    root.mainloop()


main()
