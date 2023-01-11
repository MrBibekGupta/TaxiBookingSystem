
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import globalvar
import mysql.connector


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['bid'])
    e2.insert(0, select['pickUp_address'])
    e3.insert(0, select['dropOff_address'])
    e4.insert(0, select['pickUp_time'])
    e5.insert(0, select['dropOff_date'])




def Add():
    bookingid=e1.get()
    pickUp_address = e2.get()
    dropOff_address = e3.get()
    pickUp_time = e4.get()
    dropOff_date = e5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_taxibookingsystem")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO booking (bid,pickup_address,dropoff_address,pickup_time,dropoff_date,status) VALUES (%s, %s, %s,%s,%s,'pending')"
        val = (bookingid,pickUp_address,dropOff_address,pickUp_time,dropOff_date)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Confirm trip inserted successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)

        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



def update():
    bookingid = e1.get()
    pickUp_address = e2.get()
    dropOff_address = e3.get()
    pickUp_time = e4.get()
    dropOff_date = e5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database=" project_taxibookingsystem")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update booking set pickUp_address=%s,dropOff_address=%s,pickUp_time=%s,dropOff_date=%s where bid= %s"
        val = (pickUp_address,dropOff_address,pickUp_time,dropOff_date,bookingid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Trip Updated successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()
    root.destroy()
    import makeBooking

def delete():
    bookingid = e1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_taxibookingsystem")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from booking where bid = %s"
        val = (bookingid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleted successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_taxibookingsystem")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT bid,pickup_address,dropoff_address,pickup_time,dropoff_date,status FROM booking")
    records = mycursor.fetchall()
    print(records)

    for i, (bid,pickUp_address,dropOff_address,pickUp_time,dropOff_date,status) in enumerate(records, start=1):
        listBox.insert("", "end", values=(bid,pickUp_address,dropOff_address,pickUp_time,dropOff_date,status))
        mysqldb.close()
root = Tk()
root.geometry("1230x500")
root.resizable(False,False)
root.title("Make-Booking || TBS-Taxi Booking System || Developed By Bibek Gupta")
global e1
global e2
global e3
global e4
global e5


tk.Label(root, text=" MAKE  New  BOOKING ", fg="red", font=("times new roman",30,'bold')).place(x=10, y=10)
tk.Label(root, text="Booking_id :",font=("None",10)).place(x=10, y=100)
Label(root, text="PickUp_address :",font=("None",10)).place(x=10, y=130)
Label(root, text="DropOff Address :",font=("None",10)).place(x=10, y=160)
Label(root, text="PickUp Time :",font=("None",10)).place(x=10, y=187)
Label(root,text="DropOff_date :",font=("None",10)).place(x=10,y=210)
Label(root, text=globalvar.useremail, font=("times new roman",15,'bold')).place(x=880, y=15)

e1 = Entry(root,)
e1.place(x=140, y=100)

e2 = Entry(root)
e2.place(x=140, y=130)

e3 = Entry(root)
e3.place(x=140, y=160)

e4 = Entry(root)
e4.place(x=140, y=187)

e5 = Entry(root)
e5.place(x=140, y=212)


Button(root, text="Confirm",  command=Add ,height=2, width=20,fg="white",bg="blue").place(x=500, y=70)
Button(root, text="update",  command=update, height=2, width=20,fg="white",bg="blue").place(x=500, y=120)
Button(root, text="Cancel",  height=2, width=20,fg="white",bg="blue").place(x=500, y=170)


Button(root, text="LogOut",  height=2, width=20,fg="white",bg="Red").place(x=1080, y=10)

cols = ('bid','pickUp_address','dropOff_address','pickUp_time','dropOff_date','Status')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=245)


show()
listBox.bind('<Double-Button-1>',GetValue)


root.mainloop()
