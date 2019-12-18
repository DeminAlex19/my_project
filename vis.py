t_font = "Arial-16"


def change_position(obj, size, coords_win, window_width, window_height):
    if obj.x - coords_win[0] > window_width * 3 / 4:
        coords_win[0] = obj.x - 3 * window_width / 4
    if obj.x - coords_win[0] < window_width / 4:
        coords_win[0] = obj.x - window_width / 4
    if coords_win[0] < 0:
        coords_win[0] = 0
    return coords_win


def create_image(win, obj, coords_win):
    x = obj.x - coords_win[0]
    y = obj.y - coords_win[1]
    r = obj.r
    obj.image = win.create_rectangle([x - r, y - r], [x + r, y + r], fill=obj.color)


def update_image(win, obj, coords_win):
    x = obj.x - coords_win[0]
    y = obj.y - coords_win[1]
    r = obj.r
    win.coords(obj.image, x - r, y - r, x + r, y + r)
