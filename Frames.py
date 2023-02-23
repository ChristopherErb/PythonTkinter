from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Here's the title for this program")
root.iconbitmap("C:/Users/Christopher/PycharmProjects/tkinter/LogoOnly.ico")


#removign the "text" attribute removes it but it still works
frame = LabelFrame(root, text="This is my frame", padx=50, pady=50, background="Red" )
frame.pack(padx=100, pady=100)

#puts button in the frame we created rather than the normal "root"
b = Button(frame, text="Dont click me")
b2 = Button(frame, text="Or me")
b.grid(row=0, column=0)
b2.grid(row=1,column=1)



root.mainloop()