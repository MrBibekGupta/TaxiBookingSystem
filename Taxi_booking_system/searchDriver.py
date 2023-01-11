import mysql.connector
def searchDriver(username, password):
    sql = "select * from driver_reg where username=? and password=?"
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='customer_register'
        )
        cursor = conn.cursor(prepared=True)
        cursor.execute(sql, [username, password])
        found = False
        if cursor.fetchone():
            found = True
        cursor.close()
        conn.close()
        return found
    except :
        print("error connecting to database")


