from tkinter import *

#create root widget.. Syntax = RootWidgetName = Tk()
rootW = Tk()
#creates the label.. Syntax is name = Label(rootWidgetName, text="Text here")
label1 = Label(rootW, text="This is practice text")
#packs the label.. Syntax is labelname.pack()
label1.pack()
#creates main loop.. Syntax is root name.mainloop()
rootW.mainloop()
