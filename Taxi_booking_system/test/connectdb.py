from tkinter import messagebox
import mysql.connector # pip install mysql-connector-python

try:
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="taxi_booking"
        )
    cur=con.cursor()

except Exception as ex:
    print("connection failure")
