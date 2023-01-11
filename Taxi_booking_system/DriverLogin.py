from tkinter import*
from tkinter import messagebox
import connectdb

window=Tk()
window.title("Login || TBS-Taxi Booking System || Bibek Gupta")
window.geometry('400x350')
window.configure(bg="#fff")
window.resizable (False, False)
def signin():
    username=user.get()
    password=code.get()
    print(username,password)

    try:
        # testconnect.cur.execute("SELECT * FROM %s WHERE username = '%s' and password = '%s'" %(self.userType.get(),self.username.get(), self.password.get()))
        connectdb.cur.execute("SELECT * FROM driver table where username=%s and password=%s", (username,password))
        # connectdb.cur.execute("insert into driver_database (username,password)values(%s,%s)",(username,password))
        # connectdb.con.commit()
        # messagebox.showinfo("Sucess", "user Successfully registered")
        result = connectdb.cur.fetchone()
        print(result)
        if result:
            import driverDashboard
        else:
            print("error")
    except Exception as ex:
        messagebox.showerror(
            "Error", f"Error due to : {str(ex)}")

    # if username=='driver' and password=='driver':
    #     messagebox.showinfo("successfully",'LogIn Successfully')
    # else:
    #     messagebox.showerror("Invalid",'Incorrect username and password ')




frame=Frame(window, width=390,height=650, bg="white")
frame.place(x=40,y=30)
heading=Label (frame,text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 25, 'bold'))
heading.place(x=5,y=6)

#=======================================================================================================================
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light",12))
user.place(x=25,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame (frame, width=250,height=2, bg='black'). place (x=25,y=110)

#=======================================================================================================================
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light",12))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame (frame, width=250,height=2, bg='black').place (x=25,y=180)

#=======================================================================================================================
def signin2():

    window.destroy()
    import driverDashboard

Button1=Button(frame,width=40, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place (x=25,y=209)


window.mainloop()