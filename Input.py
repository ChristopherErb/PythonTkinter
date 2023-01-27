from tkinter import *
root = Tk()

#creates e field
e = Entry(root,)
#packs E field
e.pack()
e.insert(0, "Enter your name")

#Normal button function except e.get gets the info from the e field above
def myClick():
    #creates hello variable"
    hello = "Hello " + e.get()
    #uses hello variable in text
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()


root.mainloop()