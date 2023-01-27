from tkinter import *

root = Tk()

#Labels
Label1 = Label(root, text="Row 1, column 1")
Label2 = Label(root, text="Row 2, column 2")
Label3 = Label(root, text="Row 3, column 3")
Label4 = Label(root, text="Row 4, column 4")
Label5 = Label(root, text="Row 5, column 5")
#grid labels

Label1.grid(column=1, row=1)
Label2.grid(column=2, row=2)
Label3.grid(column=3, row=3)
Label4.grid(column=4, row=4)
Label5.grid(column=5, row=5)

#mainloop
root.mainloop()