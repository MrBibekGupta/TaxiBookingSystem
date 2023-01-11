import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import sys
import mysql.connector

class CustomerRegister():
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form || TBS-Taxi Booking System || Bibek Gupta")

        # Variable
        self.name_var = StringVar()
        self.address_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = StringVar()
        self.gender_var = StringVar()
        self.id_var = StringVar()
        self.payment_var = StringVar()
        self.password = StringVar()
        self.cpassword = StringVar()
        self.check_var = StringVar()


        ##################################################################################################################
        # Title frame
        self.root.geometry('460x600')
        self.root.resizable(False, False)

        frame = Frame(self.root)
        frame.place(x=0, y=0, width=390, height=48, )
        lbl = Label(frame, text="CUSTOMER REGISTER FORM", font=("times new roman", 19, 'bold'), fg='darkblue')
        lbl.place(x=10, y=10)
        # informaiton title
        mainframe = Frame(self.root)
        mainframe.place(x=0, y=49, width=720, height=600)

        ########################################################################################################################
        # username
        username = Label(mainframe, text="Username: ", font=("times new roman", 15, 'bold'))
        username.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        self.userentry = ttk.Entry(mainframe, textvariable=self.name_var, font=("times new roman", 15, 'bold'), width=18)
        self.userentry.grid(row=0, column=1, pady=10, padx=10, sticky=W)

        # callback  and validation register
        validate_name = self.root.register(self.checkname)
        self.userentry.config(validate='key', validatecommand=(validate_name, '%p'))

        # Address
        username = Label(mainframe, text="Address: ", font=("times new roman", 15, 'bold'))
        username.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        self.addressentry = ttk.Entry(mainframe, textvariable=self.address_var, font=("times new roman", 15, 'bold'),
                                 width=18)
        self.addressentry.grid(row=1, column=1, pady=10, padx=10, sticky=W)

        # Email
        username = Label(mainframe, text="Email: ", font=("times new roman", 15, 'bold'))
        username.grid(row=2, column=0, pady=10, padx=10, sticky=W)

        self.emailentry = ttk.Entry(mainframe, textvariable=self.email_var, font=("times new roman", 15, 'bold'), width=18)
        self.emailentry.grid(row=2, column=1, pady=10, padx=10, sticky=W)

        # contact no
        username = Label(mainframe, text="Telephone No: ", font=("times new roman", 15, 'bold'))
        username.grid(row=3, column=0, pady=10, padx=10, sticky=W)

        self.contactentry = ttk.Entry(mainframe, textvariable=self.contact_var, font=("times new roman", 15, 'bold'),
                                 width=18)
        self.contactentry.grid(row=3, column=1, pady=10, padx=10, sticky=W)

        # callback  and validation register
        validate_contact = self.root.register(self.checkconotact)
        self.contactentry.config(validate='key', validatecommand=(validate_contact, '%p'))

        # Gender
        gender_lbl = Label(mainframe, text='Select Gender:', font=("times new roman", 15, 'bold'))
        gender_lbl.grid(row=4, column=0, pady=10, padx=10, sticky=W)

        gender_frame = Frame(mainframe)
        gender_frame.place(x=160, y=200, width=208, height=46)

        radio_male = Radiobutton(gender_frame, variable=self.gender_var, value='MALE', text='MALE',
                                 font=("times new roman", 12, 'bold'))
        radio_male.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.gender_var.set('MALE')

        radio_female = Radiobutton(gender_frame, variable=self.gender_var, value='FEMALE', text='FEMALE',
                                   font=("times new roman", 12, 'bold'))
        radio_female.grid(row=0, column=1, padx=10, pady=10, sticky=W)



        # Payment method
        username = Label(mainframe, text="Payment method: ", font=("times new roman", 15, 'bold'))
        username.grid(row=7, column=0, pady=10, padx=10, sticky=W)
        options = ["CASH", "ONLINE"]
        self.payment_var=StringVar()
        self.payment_var.set("Select a payment method")
        self.paymentscombobox = ttk.Combobox(mainframe,values=options, textvariable=self.payment_var, font=("times new roman", 14, 'bold'), width=21)
        self.paymentscombobox.grid(row=7, column=1, pady=10, padx=10, sticky=W)

        # Password
        password = Label(mainframe, text="Password:", font=("times new roman", 15, 'bold'))
        password.grid(row=8, column=0, padx=10, pady=10, sticky=W)

        self.entrypassword = ttk.Entry(mainframe, textvariable=self.password, font=("times new roman", 15, 'bold'), width=18)
        self.entrypassword.grid(row=8, column=1, padx=10, pady=10, sticky=W)

        # Confirm Password
        cpass = Label(mainframe, text="Confirm Password:", font=("times new roman", 15, 'bold'))
        cpass.grid(row=9, column=0, padx=10, pady=10, sticky=W)

        self.entrycpassword = ttk.Entry(mainframe, textvariable=self.cpassword,show="*", font=("times new roman", 15, 'bold'),
                                   width=18)
        self.entrycpassword.grid(row=9, column=1, padx=10, pady=10, sticky=W)

        # check frame
        check_frame = Frame(mainframe)
        check_frame.place(x=70, y=400, width=400, height=65)

        check_btn = Checkbutton(check_frame, variable=self.check_var, text='Agree Our terms & Condition',
                                font=('time new roman', 14), onvalue=1, offvalue=0)
        check_btn.grid(row=0, column=0, padx=10, sticky=W)

        self.check_lbl = Label(check_frame, text='', font=("Arial", 14), fg='red')
        self.check_lbl.grid(row=1, column=0, padx=10, sticky=W)
        def insert():
            # self.validation()
            conn = None
            sql = """INSERT INTO customer_database (username, address, email, telephone_no,payment_method,password) VALUES(%s, %s, %s, %s,%s, %s)"""
            values = (self.userentry.get(), self.addressentry.get(), self.emailentry.get(),self.contactentry.get(),self.paymentscombobox.get(),self.entrypassword.get() )
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3306',
                    user='root',
                    password='',
                    database='project_taxibookingsystem'
                )
                cursor = conn.cursor()
                cursor.execute(sql, values)
                conn.commit()
                cursor.close()
                conn.close()
                print("Customer saved")

            except:
                print("Error: ", sys.exc_info())
            finally:
                del values
                del sql
                del conn




        #Button_frame

        button_frame = Frame(mainframe, )
        button_frame.place(x=13, y=480, width=380, height=55)

        # save data

        savebtn = Button(button_frame, text="SAVE", command=insert, font=("times new roman", 16, 'bold'),width=8, cursor='hand2', bg='blue', fg='white')
        savebtn.grid(row=0, column=0, padx=5, sticky=W)


        # Edit
        editbtn = Button(button_frame, text="EDIT", font=("times new roman", 16, 'bold'), width=9, cursor='hand2',
                            bg='blue', fg='white',command=self.edit)
        editbtn.grid(row=0, column=1, padx=5, sticky=W)

        # Exit
        exittbtn = Button(button_frame, text="EXIT", font=("times new roman", 16, 'bold'), width=9, cursor='hand2',
                         bg='blue', fg='white',command=Exit)
        exittbtn.grid(row=0, column=3, padx=5, sticky=W)



###################################################################################################################################################################
    # call back function
    def checkname(self, name):
        if name.isalnum():
            return True

        if name == '':
            return False
        else:
            messagebox.showerror('Invalid', 'Not Allowed' + name[-1])
        return False

    # Checkcontact
    def checkconotact(self, contact):
        if contact.isdigit():
            return True
        if len(str(contact)) == 0:
            return True
        # else:
        #     messagebox.showinfo("Invalid",'Invalid Entry')
        #     return True

    def checkpassword(self, password):
        if len(password) <= 21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))", password):
                return True
            else:
                messagebox.showinfo('Invalid', 'Entry valid password(Example:Bibek@123')
                return False
        else:
            messagebox.showerror("Invalid", 'Password Length too small')
            return False

    def checkemail(self, email):
        if len(email) > 7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):
                return True
            else:
                messagebox.showwarning("Alert", "Invalid email enter valid user email(example:bibekg11@gmail.com")
                return False
        else:
            messagebox.showinfo('Invalid', 'Email length is  too small')

    ##################################################################################################################################################################
    # validation

    def validation(self):
        if self.name_var.get() == '':
            messagebox.showerror('Error', 'Please enter your name', parent=self.root)

        elif self.address_var.get() == '':
            messagebox.showerror('Error', 'Please enter your Address', parent=self.root)

        elif self.email_var.get() == '':
            messagebox.showerror('Error', 'Please enter your Email-ID', parent=self.root)

        elif self.contact_var.get() == '' or len(self.contact_var.get()) != 10:
            messagebox.showerror('Error', 'Please entry your Valid contact Number', parent=self.root)

        elif self.gender_var.get() == '':
            messagebox.showerror('Error', "Please choose your gender", parent=self.root)

        elif self.payment_var.get() == '':
            messagebox.showerror('Error', 'Please enter your Address', parent=self.root)

        elif self.password.get() == '':
            messagebox.showerror('Error', 'Please enter your Password', parent=self.root)

        elif self.cpassword.get() == '':
            messagebox.showerror('Error', 'Please enter your Confirm Password', parent=self.root)

        elif self.password.get() != self.cpassword.get():
            messagebox.showerror('Error', 'Password not Match', parent=self.root)

        elif self.email_var.get() != None and self.password.get() != None:
            x = self.checkemail(self.email_var.get())
            y = self.checkpassword(self.password.get())
        if (x== True) and (y == True):
            if self.check_var.get() == 0:
                self.check_lbl.config(text='Please Agree Our terms & Condition', fg='red')
            else:
                self.check_lbl.config(text='Checked', fg='green')
                messagebox.showinfo("Successfully", f'Your registration successfully completed and your '


                                                    f'Username:{self.name_var.get()} and Password:{self.password.get()}')

    def edit(self):
        # Reset the values of the entry widgets
        self.userentry.delete(0, "end")
        self.addressentry.delete(0, "end")
        self.emailentry.delete(0, "end")
        self.contactentry.delete(0, "end")
        self.paymentscombobox.delete(0, "end")
        self.entrypassword.delete(0, "end")
        self.entrycpassword.delete(0, "end")



def save():
    pass
def Exit():
    root.destroy()
    import Login

root = Tk()
obj =CustomerRegister(root)
root.mainloop()

CustomerRegister()
