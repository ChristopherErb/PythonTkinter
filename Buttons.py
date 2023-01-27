from tkinter import *

root = Tk()

#creates what the button does, has to be above where its used
def click2():

    myLabel = Label(root, text="Youve clicked a button")
    myLabel.pack()

#dont need () when using command
myButton = Button(root, text="Click me!", command=click2)
myButton.pack()

#still main loop
root.mainloop()