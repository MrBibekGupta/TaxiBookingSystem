import re
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import re
import mysql.connector
import sys

class DriverRegister():
    def __init__(self, root):
        self.root=root
        self.root.title('Registration Form')
        self.root.title("Registration Form || TBS-Taxi Booking System ||  Bibek Gupta")
        # Variable
        self.name_var=StringVar()
        self.address_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.id_var=StringVar()
        self.licenplateno_var=StringVar()
        self.password=StringVar()
        self.cpassword=StringVar()
        self.check_var=StringVar()

##################################################################################################################
        #Title frame
        self.root.geometry('460x600')
        self.root.resizable(False, False)
        frame=Frame(self.root)
        frame.place(x=0,y=0,width=390,height=48,)

        lbl=Label(frame,text="DRIVER REGISTER FORM",font=("times new roman",19,'bold'),fg='darkblue')
        lbl.place(x=10,y=10)

       #informaiton title
        mainframe = Frame(self.root)
        mainframe.place(x=0, y=49, width=720, height=600)
########################################################################################################################
        #username
        username=Label(mainframe,text="Username: ",font=("times new roman",15,'bold'))
        username.grid(row=0,column=0,pady=10,padx=10,sticky=W)

        self.userentry=ttk.Entry(mainframe,textvariable=self.name_var,font=("times new roman",15,'bold'),width=18)
        self.userentry.grid(row=0,column=1,pady=10,padx=10,sticky=W)

        #callback  and validation register
        validate_name=self.root.register(self.checkname)
        self.userentry.config(validate='key',validatecommand=(validate_name,'%p'))

        #Address
        username = Label(mainframe, text="Address: ", font=("times new roman", 15, 'bold'))
        username.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        self.addressentry = ttk.Entry(mainframe, textvariable=self.address_var,font=("times new roman", 15, 'bold'), width=18)
        self.addressentry.grid(row=1, column=1, pady=10, padx=10, sticky=W)

        #Email
        username = Label(mainframe, text="Email: ",  font=("times new roman", 15, 'bold'))
        username.grid(row=2, column=0, pady=10, padx=10, sticky=W)

        self.emailentry = ttk.Entry(mainframe,textvariable=self.email_var, font=("times new roman", 15, 'bold'), width=18)
        self.emailentry.grid(row=2, column=1, pady=10, padx=10, sticky=W)

        #contact no
        username = Label(mainframe, text="Telephone No: ", font=("times new roman", 15, 'bold'))
        username.grid(row=3, column=0, pady=10, padx=10, sticky=W)

        self.contactentry = ttk.Entry(mainframe,textvariable=self.contact_var,font=("times new roman", 15, 'bold'), width=18)
        self.contactentry.grid(row=3, column=1, pady=10, padx=10, sticky=W)

        # callback  and validation register
        validate_contact = self.root.register(self.checkconotact)
        self.contactentry.config(validate='key', validatecommand=(validate_contact,'%p'))

        #Gender
        gender_lbl=Label(mainframe,text='Select Gender:',font=("times new roman", 15, 'bold'))
        gender_lbl.grid(row=4, column=0, pady=10, padx=10, sticky=W)

        gender_frame=Frame(mainframe)
        gender_frame.place(x=160 ,y=200,width=208,height=46)

        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='MALE',text='MALE',font=("times new roman", 12, 'bold'))
        radio_male.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.gender_var.set('MALE')

        radio_female = Radiobutton(gender_frame,variable=self.gender_var, value='FEMALE', text='FEMALE', font=("times new roman", 12, 'bold'))
        radio_female.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # LICENSE NUMBER
        username = Label(mainframe, text="License Plate No: ", font=("times new roman", 15, 'bold'))
        username.grid(row=7, column=0, pady=10, padx=10, sticky=W)

        self.licensetsentry = ttk.Entry(mainframe, textvariable=self.licenplateno_var, font=("times new roman", 15, 'bold'),
                                 width=18)
        self.licensetsentry.grid(row=7, column=1, pady=10, padx=10, sticky=W)

        #Password
        password=Label(mainframe,text="Password:",font=("times new roman", 15, 'bold'))
        password.grid(row=8, column=0, padx=10, pady=10, sticky=W)

        self.entrypassword=ttk.Entry(mainframe,textvariable=self.password,font=("times new roman", 15, 'bold'),width=18)
        self.entrypassword.grid(row=8, column=1, padx=10, pady=10, sticky=W)

        #Confirm Password
        cpass=Label(mainframe,text="Confirm Password:",font=("times new roman", 15, 'bold'))
        cpass.grid(row=9, column=0, padx=10, pady=10, sticky=W)

        self.entrycpassword = ttk.Entry(mainframe,textvariable=self.cpassword,show='*', font=("times new roman", 15, 'bold'), width=18)
        self.entrycpassword.grid(row=9, column=1, padx=10, pady=10, sticky=W)

        #check frame
        check_frame=Frame(mainframe)
        check_frame.place (x=70, y=400,width=400 ,height=65)

        check_btn=Checkbutton(check_frame,variable=self.check_var,text='Agree Our terms & Condition',font=('time new roman',14) , onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)

        self.check_lbl=Label(check_frame,text='',font=("Arial",14),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

        def insert():
            self.validation()
            conn = None
            sql = """INSERT INTO driver_database (username, address, email, telephone_no,license_plate_no,password) VALUES( %s, %s, %s,%s, %s,%s)"""
            values = (self.userentry.get(), self.addressentry.get(), self.emailentry.get(),self.contactentry.get(),self.licensetsentry.get(),self.entrypassword.get() )
            # result = False
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
                print("Driver saved")
            except:
                print("Error: ", sys.exc_info())
            finally:
                del values
                del sql
                del conn


        #Button_frame
        button_frame=Frame(mainframe,)
        button_frame.place(x=13,y=480,width=380,height=55)

        #save data
        savebtn=Button(button_frame,text="SAVE",command=insert,font=("times new roman", 16, 'bold'),width=8,cursor='hand2',bg='blue',fg='white')
        savebtn.grid(row=0 , column=0, padx=5, sticky=W)

        # Edit
        displaybtn = Button(button_frame, text="EDIT",command=self.edit, font=("times new roman", 16, 'bold'), width=9, cursor='hand2',bg='blue',fg='white')
        displaybtn.grid(row=0, column=1, padx=5, sticky=W)

        # Exit
        editbtn= Button(button_frame, text="EXIT", font=("times new roman", 16, 'bold'), width=9, cursor='hand2',bg='blue',fg='white',command=Exit)
        editbtn.grid(row=0, column=3, padx=5, sticky=W ,)
###################################################################################################################################################################
    # call back function
    def checkname(self,name):
        if name.isalnum():
            return True

        if name=='':
            return False
        else:messagebox.showerror('Invalid','Not Allowed'+name[-1])
        return False

    #Checkcontact
    def checkconotact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        # else:
        #     messagebox.showinfo("Invalid",'Invalid Entry')
        #     return True

    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True
            else:
                messagebox.showinfo('Invalid','Entry valid password(Example:Bibek@123')
                return False
        else:
            messagebox.showerror("Invalid",'Password Length too small')
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
        if self.name_var.get()=='':
            messagebox.showerror('Error','Please enter your name',parent=self.root)

        elif self.address_var.get()=='':
            messagebox.showerror('Error','Please enter your Address',parent=self.root)

        elif self.email_var.get()=='':
            messagebox.showerror('Error','Please enter your Email-ID',parent=self.root)

        elif self.contact_var.get()=='' or len(self.contact_var.get())!=10:
            messagebox.showerror('Error','Please entry your Valid contact Number',parent=self.root)

        elif self.gender_var.get()=='':
            messagebox.showerror('Error',"Please choose your gender",parent=self.root)

        elif self.licenplateno_var.get()=='':
            messagebox.showerror('Error','Please enter your License Plate NO',parent=self.root)

        elif self.password.get()=='':
            messagebox.showerror('Error','Please enter your Password',parent=self.root)

        elif self.cpassword.get()=='':
            messagebox.showerror('Error','Please enter your Confirm Password',parent=self.root)

        elif self.password.get()!=self.cpassword.get():
            messagebox.showerror('Error','Password not Match',parent=self.root)

        elif self.email_var.get()!=None and self.password.get()!=None:
            x=self.checkemail(self.email_var.get())
            y=self.checkpassword(self.password.get())
        if (x== True) and (y== True):
            if self.check_var.get()==0:
                self.check_lbl.config(text='Please Agree Our terms & Condition',fg='red')
            else:
                self.check_lbl.config(text='Checked',fg='green')
                messagebox.showinfo("Successfully",f'Your registration successfully completed and your '
                     
                     
           
                                                   f'Username:{self.name_var.get()} and Password:{self.password.get()}')
    def edit(self):
        # Reset the values of the entry widgets
        self.userentry.delete(0, "end")
        self.addressentry.delete(0, "end")
        self.emailentry.delete(0, "end")
        self.contactentry.delete(0, "end")
        self.licensetsentry.delete(0, "end")
        self.entrypassword.delete(0, "end")
        self.entrycpassword.delete(0, "end")

def Exit():
    root.destroy()
    import Login

root=Tk()
obj=DriverRegister(root)
root.mainloop()






