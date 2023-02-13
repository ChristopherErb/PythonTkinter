from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Chris's Learning")

#changing icon in upper left
root.iconbitmap("C:/Users/Christopher/PycharmProjects/tkinter/LogoOnly.ico")

#using Pillow (PIL above)

my_img = ImageTk.PhotoImage(Image.open("profileFb.jpg"))

my_label = Label(image=my_img)
my_label.pack()



#creates button to exit program
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()


root.mainloop()
