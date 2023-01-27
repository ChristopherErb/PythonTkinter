#imports Tkinter
from tkinter import *
#creates root widget
root = Tk()

#creates the text label widget
myLabel = Label(root, text="Hello world")
#shoves it onto the page/screen
myLabel.pack()

#creates main loop to control everything
root.mainloop()