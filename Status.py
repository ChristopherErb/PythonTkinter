from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Chris's Learning")

#changing icon in upper left
root.iconbitmap("C:/Users/Christopher/PycharmProjects/tkinter/LogoOnly.ico")

#using Pillow (PIL above)
#change

#Created Images
my_img1 = ImageTk.PhotoImage(Image.open("images/profileFb.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/DramaOldWoman.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/FuckingIdiots.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/WinnerFuckingBlizzard.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/Tongue.jpg"))


#Put Images in list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=my_img1)

my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    #gets rid of what is on My_label
    my_label.grid_forget()


    my_label = Label(image=image_list[image_number-1])

    #update all the buttons once we click the button
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))


    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #updates status bar

    #bd = border, relief = how we sank the label, anchor e =  anchor to the East of the window
    status = Label(root, text="Image " + str(image_number) + "of "  + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #updates status bar
    status = Label(root, text="Image " + str(image_number) + "of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=back, state=DISABLED)

#creates button to exit program
button_quit = Button(root, text="Exit program", command=root.quit)

button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop()
