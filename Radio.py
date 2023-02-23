from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("This is the title")
root.iconbitmap("C:/Users/Christopher/PycharmProjects/tkinter/LogoOnly.ico")

#creates variable ot keep track
#r = IntVar()
#r.set("1")

Modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushrooms","Mushrooms"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

#Loop to create all 4 radio buttons
for text, mode in Modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    r_Label = Label(root, text=value)
    r_Label.pack()

#Radiobutton(root, text="Option1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#r_Label = Label(root, text=pizza.get())
#r_Label.pack()

click = Button(root, text="Click me", command= lambda: clicked(pizza.get()))
click.pack()

mainloop()