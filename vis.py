from tkinter import *
from PIL import ImageTk, Image
t_font = "Arial-16"


def change_position(obj, size, coords_win, window_width, window_height):
    if size > window_width:
        if obj.x - coords_win[0] > window_width * 3 / 4:
            coords_win[0] = obj.x - 3 * window_width / 4
        if obj.x - coords_win[0] < window_width / 4:
            coords_win[0] = obj.x - window_width / 4
        if coords_win[0] < 0:
            coords_win[0] = 0
        if coords_win[0] > size - window_width:
            coords_win[0] = size - window_width
    else:
        coords_win[0] = (size - window_width) / 2
    return coords_win


def create_image(win, obj, coords_win):
    x = obj.x - coords_win[0]
    y = obj.y - coords_win[1]
    r = obj.r
    if type(obj).__name__ == 'Body':
        obj.im = Image.open(obj.image)
        obj.imagetk = ImageTk.PhotoImage(obj.im)
        obj.image = win.create_image(x, y, image=obj.imagetk)
    else:
        obj.im = Image.open(obj.image)
        obj.imagetk = ImageTk.PhotoImage(obj.im)
        obj.image = win.create_image(x, y, image=obj.imagetk)


def update_image(win, obj, coords_win):
    x = obj.x - coords_win[0]
    y = obj.y - coords_win[1]
    win.coords(obj.image, x, y)
