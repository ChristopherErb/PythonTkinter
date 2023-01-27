from tkinter import *

root = Tk()

eBox = Entry(root)
eBox.pack()

def eRun():
    eHello = "Hello, " + eBox.get()
    eLabel = Label(root, text=eHello)
    eLabel.pack()


eButton = Button(root, text="Click this button", command=eRun)
eButton.pack()

root.mainloop()