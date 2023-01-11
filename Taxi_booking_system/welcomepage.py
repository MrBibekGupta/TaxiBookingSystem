# import tkinter as tk
#
# class WelcomePage(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.parent = parent
#         self.configure(bg="white")
#
#
#         # create a label to display a welcome message
#         welcome_label = tk.Label(self, text="Welcome to the Online Taxi Booking System", font=("Helvetica", 30,'bold'),fg="Black",bg="white")
#         welcome_label.pack(padx=10, pady=10)
#
#         # create a button to navigate to the booking page
#         booking_button = tk.Button(self, text="Book a Taxi",command=makebooking,bg="blue",fg="white",height=2,width=20,font=("Helvetica", 10,'bold'))
#         booking_button.pack(padx=10, pady=10)
#         booking_button = tk.Button(self, text="Exit", command=Exit,bg="red",fg="white",height=2,width=20,font=("Helvetica", 10,'bold'))
#         booking_button.pack(padx=10, pady=10)
# def Exit():
#     root.destroy()
#     import Login
# def makebooking():
#     root.destroy()
#     import makeBooking
#
#
# # create the root window
# root = tk.Tk()
# root.title("Taxi Booking System")
# # create a dictionary to store the frames for each page
# frames = {}
#
# # create the welcome page and add it to the dictionary
# welcome_page = WelcomePage(root)
# frames["WelcomePage"] = welcome_page
#
# # add the welcome page to the root window
# welcome_page.pack()
#
# # start the event loop
# root.mainloop()
#
