from tkinter import *


root = Tk()
root.title("Calculator Practice")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
    return

button_1 = Button(root, text="1", padx=40, pady=20, command=button_add)
button_2 = Button(root, text="2", padx=40, pady=20, command=button_add)
button_3 = Button(root, text="3", padx=40, pady=20, command=button_add)

button_4 = Button(root, text="4", padx=40, pady=20, command=button_add)
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add)
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add)

button_7 = Button(root, text="7", padx=40, pady=20, command=button_add)
button_8 = Button(root, text="8", padx=40, pady=20, command=button_add)
button_9 = Button(root, text="9", padx=40, pady=20, command=button_add)

button_0 = Button(root, text="0", padx=40, pady=20, command=button_add)
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)

button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_add)
button_equals = Button(root, text="=",padx="140", pady="20", command=button_add)


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


root.mainloop()