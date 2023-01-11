import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

root = Tk()
root.geometry("1550x400")
root.title("Assign Driver|| TBS-Taxi Booking System || Developed By Bibek Gupta")
global e1

def prt():
    var1 = e1.get()
    print(var1)

tk.Label(root, text=" Assign Driver ",bg="brown",fg="white",width=100, font=("times new roman",20,'bold')).place(x=10, y=10)

tk.Label(root,text="Search Driver:").place(x=100,y=100)

Label(root, text="admin@gamil.com", font=("times new roman",15,'bold'),bg="brown",fg='white').place(x=1150, y=15)

e1 = Entry(root)
e1.place(x=200, y=100)


Button(root, text="Search",  height=1, width=10,fg="white",bg="blue",command=prt).place(x=350, y=100)
Button(root, text="LogOut",  height=1, fg="white",bg="brown",font=("times new roman",10)).place(x=1400, y=15)

cols = ('booking ID',  'pickup date', 'pickup time', 'pickup address', 'dropoff address', 'Driver number','Diver number ','bookstatus')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=1, y=170)



root.mainloop()
