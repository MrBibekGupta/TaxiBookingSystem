import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

root = Tk()
root.geometry("1430x600")
root.resizable(False,False)
root.title("View-Driver-Date || TBS-Taxi Booking System || Developed By Bibek Gupta")
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
tk.Label(root, text=" View Driver ", fg="red", font=("times new roman",20,'bold')).place(x=10, y=10)

tk.Label(root, text="Driver ID :").place(x=200, y=110)
Label(root, text=" Username:").place(x=200, y=140)
Label(root, text="Address :").place(x=200, y=170)
Label(root, text="Email :").place(x=200, y=200)
Label(root,text="Telephone :").place(x=200,y=230)
Label(root,text="License No").place(x=200,y=260)
Label(root,text="password :").place(x=200,y=290)
Label(root,text="Search Driver:").place(x=450,y=30)

Label(root, text="admin@gamil.com:", font=("times new roman",15,'bold')).place(x=880, y=15)



e1 = Entry(root)
e1.place(x=300, y=110)

e2 = Entry(root)
e2.place(x=300, y=140)

e3 = Entry(root)
e3.place(x=300, y=170)

e4 = Entry(root)
e4.place(x=300, y=200)

e5 = Entry(root)
e5.place(x=300, y=230)

e6 = Entry(root)
e6.place(x=300, y=290)

e7 = Entry(root)
e7.place(x=550, y=35)

e8 = Entry(root)
e8.place(x=300, y=260)



Button(root, text="Save",  height=2, width=20,fg="white",bg="blue",).place(x=700, y=100)
Button(root, text="update",  height=2, width=20,fg="white",bg="blue").place(x=700, y=150)
Button(root, text="delete",  height=2, width=20,fg="white",bg="blue").place(x=700, y=200)
Button(root, text="Cancel",  height=2, width=20,fg="white",bg="blue").place(x=700, y=250)
Button(root, text="Search",  height=1, width=10,fg="white",bg="blue").place(x=700, y=30)
Button(root, text="LogOut",  height=2, width=20,fg="white",bg="Red").place(x=1050, y=10)

cols = (' driver Id','Name','Address','Email','Telephone No','Licence No','Password')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=370)



root.mainloop()
