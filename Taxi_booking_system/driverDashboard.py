import tkinter as tk
import datetime
from tkinter import ttk

class ViewBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("View Booking || TBS-Taxi Booking System || Developed By Bibek Gupta")
        self.tittle =tk.Label(root,text="Driver Dashboard",bg="blue",fg="white",width=95,height=1,font=("times new roman",20,'bold'))
        self.tittle.place(x=5,y=5)
        self.root.geometry('1510x500')

        # Display current date and time
        now = datetime.datetime.now()
        self.date_time_label = tk.Label(root, text=now.strftime("%m/%d/%Y %I:%M %p"),font=("times new roman",15,"bold"),bg="blue",fg="white")
        self.date_time_label.place(x=10, y=10)

        # Create Treeview to display data
        self.tree = ttk.Treeview(root, columns=('bookingID', 'customerName', 'pdate', 'ptime', 'paddress', 'daddress', 'bstatus'))
        self.tree.place(x=5, y=155)
        self.tree.heading('#0', text='Booking ID')
        self.tree.heading('#1', text='Customer Name')
        self.tree.heading('#2', text='Pickup Date')
        self.tree.heading('#3', text='Pickup Time')
        self.tree.heading('#4', text='Pickup Address')
        self.tree.heading('#5', text='Destination Address')
        self.tree.heading('#6', text='Booking Status')

        # Insert data into the Treeview
        self.tree.insert("", "end", text="B001", values=("B001", "John Smith", "01/01/2023", "12:00 PM", "123 Main St", "456 Market St", "In Progress"))
        self.tree.insert("", "end", text="B002", values=("B002", "Jane Doe", "01/02/2023", "1:00 PM", "789 Broad St", "321 Park Ave", "Completed"))
        #create driver email
        self.driver_email = tk.Label(root,text="globalvar.driveremail")
        self.driver_email.place(x=900,y=40)
        # Create driver active/inactive indicator
        self.driver_status = tk.Label(root, text="Driver Status")
        self.driver_status.place(x=20, y=55)

        # Create On/Off button
        self.on_off_button = tk.Button(root, text="On/Off", command=self.toggle_driver,bg='red')
        self.on_off_button.place(x=20, y=90)


    def toggle_driver(self):

     if self.on_off_button["text"] == "ON":
        self.on_off_button["text"] = "OFF"
        self.driver_status["text"] = "Driver Status: ACTIVE"
        self.on_off_button["state"] = "disabled"
     else:
        self.on_off_button["text"] = "ON"
        self.driver_status["text"] = "Driver Status: INACTIVE"
        self.on_off_button["state"] = "normal"

     # Create Complete button
        self.complete_button = tk.Button(root, text="Complete", command=self.complete_booking,bg="Green")
        self.complete_button.place(x=1400, y=90)

    def complete_booking(self):
        # code to complete booking goes here
        selected_item = self.tree.focus()

        # Update bstatus column in Treeview
        self.tree.set(selected_item, column="bstatus", value="Completed")

root = tk.Tk()
view_booking = ViewBooking(root)
root.mainloop()
