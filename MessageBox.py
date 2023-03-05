from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Message Boxes!")
root.iconbitmap("images/LogoOnly.ico")

#types of boxes showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
#first is the title,  second is what it says
def popup():
    response = messagebox.askyesno("This is my Popup!","Hello world")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()

Button(root, text="Popup", command=popup).pack()



mainloop()