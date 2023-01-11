from tkinter import*
from tkinter import messagebox
import connectdb
window=Tk()
window.title('Login')
window.geometry('450x350')
window.configure(bg="#fff")
window.resizable (False, False)

def signin():
    username=user.get()
    password=code.get()
    print(username,password)

    try:

        connectdb.cur.execute("SELECT * FROM customer_database where username=%s and password=%s", (username,password))

        messagebox.showinfo("Successfully", "Customer Successfully LogIn")
        result = connectdb.cur.fetchone()
        print(result)
        if result:
            import makeBooking
        else:
            print("error")
    except Exception as ex:
        messagebox.showerror(
            "Error", f"Error due to : {str(ex)}")


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


Button1=Button(frame,width=40, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place (x=25,y=209)
label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place (x=35,y=265)
def signup():
    import Mainpage
sign_up= Button (frame, width=10, text="Sign Up", border=0, bg='white', cursor= 'hand2', fg='#57a1f8', command=signup)
sign_up.place(x=170,y=265)

def admin():
    import Admin
admin=Button(frame,width=10, text="Admin", border=0, bg='white', cursor= 'hand2', fg='#57a1f8',command=admin)
admin.place(x=290,y=265)


def driver():
    import DriverLogin
driver=Button(frame,width=9, text="Driver", border=0, bg='white', cursor= 'hand2', fg='#57a1f8',command=driver)
driver.place(x=230,y=265)



window.mainloop()