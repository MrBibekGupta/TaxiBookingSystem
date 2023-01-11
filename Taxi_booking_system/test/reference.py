def show(self):
    connectDB
    try:
        connectDB.cur.execute(
            "SELECT trip_id,pickup_date,pickup_time,pickup_address,dropoff_address,trip_status,driver_id FROM `trip` WHERE passenger_id = %s " % (
                self.pid.get()))
        rows = connectDB.cur.fetchall()
        self.Table.delete(*self.Table.get_children())
        for row in rows:
            self.Table.insert('', END, values=row)

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)