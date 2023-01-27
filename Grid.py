from tkinter import *
#creates the root widget
root = Tk()
#creates labels
myLabel1 = Label(root, text="First label text")
myLabel2 = Label(root, text="    2      ")
myLabel3 = Label(root, text="    3      ")
myLabel4 = Label(root, text="Second label text")
#places labels on the grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)
myLabel4.grid(row=3, column=3)
#creates mainloop
root.mainloop()

