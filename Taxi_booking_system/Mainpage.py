import tkinter as tk

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry('650x300')
        self.root.resizable(False, False)
        self.root.title("MainPage || TBS-Taxi Booking System || Developed By Bibek Gupta")
        # Create the main frame
        self.frame = tk.Frame(self.root)

        # Create the Welcome label
        self.welcome_label = tk.Label(self.frame, text="Welcome to online Taxi_Booking_system",fg='red', font=("Times New Roman", 17),width=30,height=0,bd=3)
        self.welcome_label2 = tk.Label(self.frame, text=" REGISTER YOUR ACCOUNT ", fg='blue',font=("Times New Roman", 16), width=35, height=3,)

        self.customer_button = tk.Button(self.frame, text="Customer Registration",font=('Georgia'), width=25,bg='#800080',fg='white',command=customerregistration)
        self.driver_button = tk.Button(self.frame, text="Driver Registration",font=('Georgia'), width=25,bg='#800080',fg='white',command=driverregistration)
        self.exit_button = tk.Button(self.frame, text="Exit",font=('Georgia'), width=25,bg='#FF0000',fg='white', command=self.root.destroy)

        # Add the widgets to the frame
        self.welcome_label.pack()
        self.welcome_label2.pack()
        self.customer_button.pack()
        self.driver_button.pack()
        self.exit_button.pack()

        # Add the frame to the main window
        self.frame.pack()

def customerregistration():
    root.destroy()
    import customer_registration_form

def driverregistration():
    root.destroy()
    import Driver_Registration_form

# Create the main window
root = tk.Tk()

# Create an instance of the MainPage class
app = MainPage(root)

# Run the main loop
root.mainloop()
