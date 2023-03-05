from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Here's the title")


global Grand_total
#interger variable
#r = IntVar()
#r.set("2")


MODES = [
    ("Flea","Flea","10"),
    ("Fix","Fix", "90"),
    ("Exam","Exam", "150"),
    ("Euth","Euth", "0"),
]

services = StringVar()
services.set("Flea")


#For loop that cycles through the list and touples in MODES above

for text, mode, price in MODES:
    Radiobutton(root, text=text, variable=services, value=int(price)).pack(anchor=W)

def clicked(value):
    global Grand_total
    Grand_total = value + Grand_total
    myLabel = Label(root, text=Grand_total)
    myLabel.pack()

#Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=services.get())
#myLabel.pack()

myButton = Button(root, text="Add Services", command=lambda: clicked(services.get()))
myButton.pack()


mainloop()