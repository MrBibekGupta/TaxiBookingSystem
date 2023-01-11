import tkinter as tk

class Admin:
    def __init__(self, window):
        self.window = window
        self.window.title("Admin page")
        self.window.geometry("1000x590")
        self.window.configure(bg="white")
        self.window.resizable(False, False)
        self.window.title("ADMIN || TBS-Taxi Booking System || Developed By Bibek Gupta")

        # Create a label for the frame
        self.label = tk.Label(self.window, text="TBS-Taxi Booking System",font=("times new roman", 30, 'bold'),width=200,height=1,bg="purple",fg="black")
        self.label.pack()
        self.label = tk.Label(self.window, text="", font=("times new roman", 30, 'bold'),
                              width=200, height=1, bg="white", fg="black")
        self.label.pack()

        self.label = tk.Label(self.window, text="ADMIN", font=("times new roman", 28, 'bold'), width=200, height=1,
                              bg="white", fg="blue")
        self.label.pack()

        # Create a frame for the buttons
        self.label = tk.Label(self.window, text="", font=("times new roman", 30, 'bold'),
                              width=200, height=1, bg="white", fg="black")
        self.label.pack()
        self.frame = tk.Frame(self.window,width=200,height=100,bd=5,bg='white')
        self.frame.pack()

        # Create the buttons
        self.viewbook_button = tk.Button(self.frame, text="Assign Book",command=viewallbook, bg='blue',pady=12,padx=12,fg='white',font=("times new roman",12,'bold'))
        self.viewcustomer_button = tk.Button(self.frame, text="Viewcustomer",command=viewcustomer, bg='blue',pady=12,padx=12, fg='white',font=("times new roman",12,'bold'))
        self.viewdriver_button = tk.Button(self.frame, text="ViewTaxidriver",command=viewdriver, bg='blue',pady=12,padx=12, fg='white',font=("times new roman",12,'bold'))
        self.exit_button = tk.Button(self.frame, text="Logout", command=exit,bg='red',pady=12,padx=12, fg='white',font=("times new roman",12,'bold'))

        # Use the .grid() method to place the buttons in a single row
        self.viewbook_button.grid(row=0, column=0 , padx=15,pady=15)
        self.viewcustomer_button.grid(row=0, column=1,padx=15,pady=15)
        self.viewdriver_button.grid(row=0, column=2,padx=15,pady=15)
        self.exit_button.grid(row=0, column=3,padx=15,pady=15)

def viewallbook():
    pass


def viewcustomer():
    pass

def viewdriver():
    pass

def exit():
    window.destroy()


# Create the main window
window = tk.Tk()

# Create an instance of the Admin class
admin = Admin(window)

# Run the main loop
window.mainloop()
