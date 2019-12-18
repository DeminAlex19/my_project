from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('200x200')
c = Canvas(root, width=200, height=200)
c.pack()
pill = Image.open('ground.gif')
image = ImageTk.PhotoImage(pill)
imagesprite = c.create_image(100, 100, image=image)
root.mainloop()

root.mainloop()