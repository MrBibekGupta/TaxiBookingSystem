# import tkinter as tk
# class CustomerGUI:
#     def __init__(self, root):
#         self.root = root
#         # Set the background color and font for the GUI
#         self.root.configure(bg='white')
#         self.root.option_add("*Font", "Helvetica 12")
#         self.root.geometry('450x200')
#         # self.root.resizable(False, False)
#
#         self.root.title("CustomerPage")
#
#         # Create a frame for the welcome message
#         self.welcome_frame = tk.Frame(self.root, bg='white')
#         self.welcome_frame.pack(side='top', fill='x')
#
#         # Add a label to the welcome frame with a welcome message
#         self.welcome_label = tk.Label(self.welcome_frame, text=" Welcome to the Online Taxi Booking System\n ",font=("Times New Roman", 16,'bold'), bg='white',fg="red",)
#         self.welcome_label.pack(side='left',pady=10)
#
#         # Create a frame for the buttons
#         self.button_frame = tk.Frame(self.root, bg='white')
#         self.button_frame.pack(side='top', fill='x')
#
#         # Create the four buttons
#         self.make_booking_button = tk.Button(self.button_frame, text="Book a Trip ", bg='blue',fg="white",font=("Times New Roman", 13),command=Bookatrip,)
#         self.update_customer_button = tk.Button(self.button_frame, text="Update Customer", bg='blue',fg="white",font=("Times New Roman", 13))
#         self.delete_customer_button = tk.Button(self.button_frame, text="Delete Customer", bg='blue',fg="white",font=("Times New Roman", 13))
#         self.logout_button = tk.Button(self.button_frame, text="Logout",bg='red',fg="white",font=("Times New Roman", 13))
#
#         # Use the .grid() geometry manager to place the buttons in a single row
#         self.make_booking_button.grid(row=0, column=0)
#         self.update_customer_button.grid(row=0, column=1)
#         self.delete_customer_button.grid(row=0, column=2)
#         self.logout_button.grid(row=0, column=3)
#
# def Bookatrip():
#     root.destroy()
#
#
# # Create the root window
# root = tk.Tk()
#
# # Create an instance of the CustomerGUI class
# app = CustomerGUI(root)
#
# # Run the main loop
# root.mainloop()
#
#
#
