import tkinter
from classes import *
from vis import *
from tkinter.filedialog import *
from files_treatment import *
from movement import *

root = tkinter.Tk()
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry(str(window_width) + 'x' + str(window_height))
window = None
frame = None

list_levels = ['Level 1','Level 2', 'Level 3']
level_objects = []
size_level = 0
coords_win = [0, 0]
hero = None

flag_perform = False
'''Флаг основногой цикличности'''
level_time = 0
'''Время уровня'''
time_step = 10

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
    global next_level_button

    level_time += time_step

    if press_button_right:
        hero.vx = 1
    if press_button_left:
        hero.vx = -1
    if press_button_up and checkground(hero, level_objects):
        hero.vy = -6
    if press_button_down:
        hero.typeattack = 'fall'
        hero.vy = max(1, hero.vy)
    if press_button_special:
        special(hero)
        press_button_special = False
    if press_button_act and press_button_special != True:
        action(hero)
        press_button_act = False
    if hero.status == 'level end':
        level_end()
    if hero.life <= 0:
        game_end()
    move(level_objects)
    size_level = count_size_level(level_objects)
    coords_win = change_position(hero, size_level, coords_win, window_width, window_height)
    for obj in level_objects:
        update_image(window, obj, coords_win)
    if flag_perform:
        window.after(time_step, execution)

def game_end():
    global game_over_label
    global flag_perform
    flag_perform = False
    pause_button.pack_forget()
    game_over_label.pack()
    screen_pause = window.create_rectangle([0, 0], [window_width, window_height], fill='black')
    new_game_button.pack()
    exit_button.pack()
    print(1)

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
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button
    flag_perform = True
    level_time = 0
    for button in menu_level_button:
        button.pack_forget()
    menu_record_button.pack_forget()
    new_game_button.pack_forget()
    pause_button.pack()
    next_level_button.pack_forget()
    level_objects = read_level(level_name)
    hero = find_hero(level_objects, hero)
    size_level = count_size_level(level_objects)
    coords_win = [window_width/2, 0]
    coords_win = change_position(hero, size_level, coords_win, window_width, window_height)
    for obj in level_objects:
        create_image(window, obj, coords_win)
    root.bind('<KeyPress>', checkPress)
    root.bind('<KeyRelease>', checkRelease)
    execution()
    # удаление меню, создание уровня из файла, создание кнопки паузыб запуск выполнения


def stop_execution():
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button
    flag_perform = False
    pause_button.pack_forget()
    screen_pause = window.create_rectangle([0, 0], [window_width, window_height], fill='black')
    continue_button.pack()
    new_game_button.pack()
    exit_button.pack()
    # остановка выполнения и создание кнопки продолжения


def continue_execution():
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button
    flag_perform = True
    window.delete(screen_pause)
    continue_button.pack_forget()
    pause_button.pack()
    execution()
    # Удаление кнопки продолжения и запуск выполнения

def start_screen():
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button
    global new_game_button

    level_objects = []

    name_label.pack_forget()
    name_entry.pack_forget()
    play_button.pack_forget()
    exit_button.pack_forget()
    next_level_button.pack_forget()
    new_game_button.pack_forget()
    continue_button.pack_forget()
    window.pack(fill=BOTH, expand=1)
    name_label.pack()
    name_entry.pack()
    play_button.pack()
    exit_button.pack()
    menu_record_button.pack()



def level_choice():
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button

    name_label.pack_forget()
    name_entry.pack_forget()
    play_button.pack_forget()
    exit_button.pack_forget()
    next_level_button.pack_forget()

    level_objects = []
    for button in menu_level_button:
        button.pack()


def level_end():
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button
    global new_game_button


    flag_perform = False
    pause_button.pack_forget()
    screen_pause = window.create_rectangle([0, 0], [window_width, window_height], fill='black')
    next_level_button.pack()
    exit_button.pack()
    new_game_button.pack()


def main():
    global time_step
    global window
    global menu_level_button
    global menu_record_button
    global pause_button
    global frame
    global next_level_button
    global play_button
    global exit_button
    global name_entry
    global name_label
    global level_objects
    global hero
    global menu_record_button
    global window
    global frame
    global screen_pause
    global flag_perform
    global continue_button
    global pause_button
    global next_level_button
    global new_game_button
    global game_over_label

    window = tkinter.Canvas(root, bg='black')
    frame = tkinter.Frame(root)
    frame.pack(side=TOP)
    name = tkinter.Label(frame, text="The Nario", width=10, bg='yellow', fg='red', font=('Arial 32', 10, 'bold'))
    name.pack(side=RIGHT)
    level_objects = []
    name_hero = StringVar()
    name_label = Label(window, text='Enter your name:')
    name_entry = Entry(window, textvariable=name_hero)
    play_button = Button(window, text='Play', command=level_choice)
    exit_button = Button(window, text='Exit', command=exit)
    menu_record_button = Button(window, text='View the high score table', command=view_scores)
    pause_button = tkinter.Button(window, text='Pause', command=stop_execution)
    continue_button = tkinter.Button(window, text='Continue', command=continue_execution, width=10)
    next_level_button = Button(window, text='Choose a level', command=level_choice)
    new_game_button = Button(window, text='New game', command=start_screen)
    game_over_label = Label(window,text='Game over',font=20)
    for level in list_levels:
        menu_level_button.append(
            tkinter.Button(window, text=level, command=lambda level_name=level: start_level(level_name)))

    start_screen()
    root.mainloop()


main()
