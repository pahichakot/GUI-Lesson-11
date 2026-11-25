#Theme Changer
from tkinter import *

#Setup
root = Tk()
root.geometry("300x300")
root.title("Theme Changer")

#Background Color - Label
background_color = Label(root, text = "Choose a background color: ", font = ("Times New Roman", 14, "normal"))
background_color.pack(pady = 10)

#Radio buttons
colors = StringVar()

#Red - Radio Button
red = Radiobutton(root, text = "red", variable = colors, value = "red")
red.pack(pady = 20)

#Green - Radio Button
green = Radiobutton(root, text = "green", variable = colors, value = "green")
green.pack(pady = 20)

#Blue - Radio Button
blue = Radiobutton(root, text = "blue", variable = colors, value = "blue")
blue.pack(pady = 20)

#Background - function
def background():
    bg_color = colors.get()
    root.config(background = bg_color)

#Apply - Button
apply = Button(root, text = "Apply", command = background)
apply.pack(pady = 20)

root.mainloop()