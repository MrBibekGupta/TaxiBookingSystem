from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
class TBS:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1920x1080+0+0")
        self.root.state('zoomed')
        self.root.title("TBS-Taxi Booking System || Developed By Sailesh Rokaya")
        self.root.config(bg="#2E4CC5")
        # ===========================All Variables===========
        # self.var_email=StringVar()
        self.var_password = StringVar()
        self.var_utype = StringVar()
        # var_email=StringVar()
        self.var_email = StringVar()
        #============CLOCK==================
        self.lbl_clock = Label(self.root, text="Welcome to Taxi Booking System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("time new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        #==============loginFrame===========
        Frame_Login = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame_Login.place(x=1210, y=110, width=315, height=640)

        # ===============ComboBoxForGender-Row-1==============================
        txt_Utype = ttk.Combobox(Frame_Login, textvariable=self.var_utype,
                                 values=("Select UserType", "Customer", "Driver", "Employee"), state='readonly',
                                 justify=CENTER, font=("Andalus", 10))
        txt_Utype.place(x=65, y=100, width=200, height=30)
        txt_Utype.current(0)

        # ===============Label==============
        loginTitel = Label(Frame_Login, text="Login System", font=("Elephant", 30, "bold"), bg="white").place(x=0, y=30,
                                                                                                              relwidth=1)
        lbl_email = Label(Frame_Login, text="Email*", bg="white", font=("Andalus", 15), fg="#767171").place(x=0, y=150,
                                                                                                            relwidth=1)
        lbl_password = Label(Frame_Login, text="Password*", bg="white", font=("Andalus", 15), fg="#767171").place(x=0,
                                                                                                                  y=230,
                                                                                                                  relwidth=1)
        lbl_hr = Label(Frame_Login, bg="lightgray").place(x=38, y=490, width=250, height=2)

        lbl_hrOR = Label(Frame_Login, text="OR", bg="white", font=("times new roman", 15, "bold")).place(x=150, y=475)
        lbl_member = Label(Frame_Login, text="Don't have an account?", bg="white", font=("times new roman", 10)).place(
            x=80, y=535)
        # ===============TextBox==============
        txtemail = Entry(Frame_Login, textvariable=self.var_email, font=("Andalus", 10), bg="white",
                         fg="#767171").place(x=65, y=190, width=200, height=30)
        txtpassword = Entry(Frame_Login, textvariable=self.var_password, font=("Andalus", 10), bg="white", show="*",
                            fg="#767171").place(x=65, y=280, width=200, height=30)
        # ============btn_logout=========
        btn_logIn = Button(Frame_Login, text="LogIn", command=self.LogIn, font=("time new roman", 15, "bold"),
                           bg="#418BCA", activebackground="#418BCA", cursor="hand2").place(x=65, y=350, height=35,
                                                                                           width=200)
        btn_cancel = Button(Frame_Login, text="Cancel", command=quit, font=("time new roman", 15, "bold"), bg="#C42F11",
                            activebackground="#C42F11", cursor="hand2").place(x=65, y=420, height=35, width=200)
        btn_forgot = Button(Frame_Login, text="Forgot Password?", command=self.forgotPassword,
                            font=("time new roman", 10), bd=0, bg="white", activebackground="white", fg="#418BCA",
                            activeforeground="#418BCA", cursor="hand2").place(x=95, y=500, height=35, width=150)
        btn_Signup = Button(Frame_Login, text="Sign Up", command=self.reg, font=("time new roman", 10), bd=0,
                            bg="white", activebackground="white", fg="#418BCA", activeforeground="#418BCA",
                            cursor="hand2").place(x=210, y=529, height=35, width=60)

        # ============Footer====================
        lbl_footer = Label(self.root,
                           text="TBS-Taxi Booking System || Developed By Sailesh Rokaya\n For Technical Support Student ID: 2020426 ",
                           font=("time new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        self.update_date_time()

    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Taxi Booking System\t\t Date:{str(date_)} \t\t Time:{str(time_)} ")
        self.lbl_clock.after(200, self.update_date_time)

    def DashboardFunc(self, email):
        # self.root.destroy()
        self.new_win = Toplevel(self.root)
        self.new_obj = DashboardClass(self.new_win, email)
        self.root.withdraw()

    def BookingFunc(self, email):
        # email=self.var_email.get()
        self.new_win = Toplevel(self.root)
        self.new_obj = bookTripClass(self.new_win, email)

    def driverDahsboard(self, email):
        self.new_win = Toplevel(self.root)
        self.new_obj = DriverDashboardClass(self.new_win, email)

    def forgotPassword(self):
        # self.root.destroy()
        self.new_win = Toplevel(self.root)
        self.new_obj = forgotPasswordClass(self.new_win)

if __name__=="__main__":
    obj=TBS()
    mainloop()



