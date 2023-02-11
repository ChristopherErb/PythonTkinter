from tkinter import *


root = Tk()
root.title("Calculator Practice")

e = Entry(root, width=35, font=('Arial', 15),  borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global math
    math = "addition"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    global math
    math = "subtraction"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    global math
    math = "division"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    global math
    math = "multiplication"
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)


    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math =="subtraction":
        e.insert(0, f_num - int(second_number))
    elif math =="division":
        e.insert(0, f_num / int(second_number))
    elif math =="multiplication":
        e.insert(0, f_num * int(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root,  text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root,  text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root,   text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root,  text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root,   text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root,   text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root,  text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root,  text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_mult = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_div = Button(root, text="/", padx=40, pady=20, command=button_divide)

button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_clear)
button_equals = Button(root, background="green",  text="=", padx="140", pady="20", command=button_equal)


button_1.grid(column=0, row=1)
button_2.grid(column=1, row=1)
button_3.grid(column=2, row=1)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

button_7.grid(column=0, row=3)
button_8.grid(column=1, row=3)
button_9.grid(column=2, row=3)

button_0.grid(column=0, row=4)
button_add.grid(column=1, row=4)
button_clear.grid(column=2, row=4)

button_equals.grid(column=0, row=5, columnspan=3)

button_sub.grid(column=0, row=6)
button_div.grid(column=1, row=6)
button_mult.grid(column=2, row=6)


root.mainloop()