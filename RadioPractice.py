from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Here's the title")

#interger variable
r = IntVar()
r.get()

Radiobutton(root, text="option 1", variable=r, value=1).pack()
Radiobutton(root, text="option 2", variable=r, value=2).pack()




mainloop()