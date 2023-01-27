from tkinter import *

root = Tk()

def click1():
    lClick1 = Label(root, text="Correct")
    lClick1.place(x=100, y=200)

def click2():
    lClick2 = Label(root, text="Wrong")
    lClick2.place(x=310, y=310)

b1 = Button(root, text="Click me", command=click1)
b2 = Button(root, text="Click me", command=click2)
b3 = Button(root, text="Click me", command=click2)
b4 = Button(root, text="Click me", command=click2)
b5 = Button(root, text="Click me", command=click2)
b6 = Button(root, text="Click me", command=click2)
b7 = Button(root, text="Click me", command=click2)
b8 = Button(root, text="Click me", command=click2)
b9 = Button(root, text="Click me", command=click2)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)




root.mainloop()