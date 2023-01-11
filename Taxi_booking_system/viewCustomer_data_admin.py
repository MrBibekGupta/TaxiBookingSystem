import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Customer ID '])
    e2.insert(0, select['pickUp_address'])
    e3.insert(0, select['dropOff_address'])
    e4.insert(0, select['pickUp_Time '])
    e5.insert(0, select['dropOff_date'])


def Add():
    CustomerId = e1.get()
    pickUp_address = e2.get()
    dropOff_address = e3.get()
    pickUp_time = e4.get()
    dropOff_date = e5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_taxibookingsystem")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO make_booking_database ( Id,pickUp_address,dropOff_address,pickUp_time,dropOff_date) VALUES (%s, %s, %s, %s,%s)"
        val = (CustomerId,pickUp_address,dropOff_address,pickUp_time,dropOff_date)
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
    CustomerId = e1.get()
    pickUp_address = e2.get()
    dropOff_address = e3.get()
    pickUp_time = e4.get()
    dropOff_date = e5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database=" project_taxibookingsystem")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  make_booking_database set  Id=%s,pickUp_address=%s,dropOff_address=%s,pickUp_time=%s,dropOff_date=%s where id= %s"
        val = (pickUp_address,dropOff_address,pickUp_time,dropOff_date,CustomerId)
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


def delete():
    CustomerId = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_taxibookingsystem")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from make_booking_database where id = %s"
        val = (CustomerId,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleted successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_taxibookingsystem")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT  Id,pickUp_address,dropOff_address,pickUp_time,dropOff_date FROM make_booking_database")
    records = mycursor.fetchall()
    print(records)

    for i, (Id,pickUp_address,dropOff_address,pickUp_time,dropOff_date) in enumerate(records, start=1):
        listBox.insert("", "end", values=(Id,pickUp_address,dropOff_address,pickUp_time,dropOff_date))
        mysqldb.close()


root = Tk()
root.geometry("1220x600")
root.resizable(False,False)
root.title("View-Customer_Date || TBS-Taxi Booking System || Developed By Bibek Gupta")
global e1
global e2
global e3
global e4
global e5
global e6
global e7
tk.Label(root, text=" View Customer ", fg="white",width=70,bg='sky blue', font=("times new roman",20,'bold')).place(x=10, y=10)

tk.Label(root, text="Customer ID :").place(x=200, y=140)
Label(root, text=" Username:").place(x=200, y=170)
Label(root, text="Address :").place(x=200, y=200)
Label(root, text="Email :").place(x=200, y=230)
Label(root,text="Telephone :").place(x=200,y=260)
Label(root,text="password :").place(x=200,y=290)
Label(root,text="Search Customer:").place(x=450,y=80)

Label(root, text="admin@gamil.com:", font=("times new roman",15,'bold',),bg="sky blue",fg="white").place(x=880, y=15)



e1 = Entry(root)
e1.place(x=300, y=140)

e2 = Entry(root)
e2.place(x=300, y=170)

e3 = Entry(root)
e3.place(x=300, y=200)

e4 = Entry(root)
e4.place(x=300, y=230)

e5 = Entry(root)
e5.place(x=300, y=260)

e6 = Entry(root)
e6.place(x=300, y=290)

e7 = Entry(root)
e7.place(x=550, y=80)


Button(root, text="Save",  height=2, width=20,fg="white",bg="blue",).place(x=700, y=150)
Button(root, text="update",  height=2, width=20,fg="white",bg="blue").place(x=700, y=200)
Button(root, text="delete",  height=2, width=20,fg="white",bg="blue").place(x=700, y=250)
Button(root, text="Cancel",  height=2, width=20,fg="white",bg="blue").place(x=700, y=300)
Button(root, text="Search",  height=1, width=10,fg="white",bg="blue").place(x=700, y=75)
Button(root, text="LogOut",  height=2, width=22,fg="white",bg="Red",font=(None,8,'bold')).place(x=1050, y=10)

cols = (' Customer Id','Name','Address','Email','Telephone No','Password')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=370)



root.mainloop()
