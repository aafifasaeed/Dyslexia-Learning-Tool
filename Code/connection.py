import asyncio
import pyodbc
import datetime

curr_date=datetime.date.today()
curr_time = datetime.datetime.now().time().strftime('%H:%M')
def con_insert(user,game,score):
    #s=int(score)
    try:
        con_string=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\92333\\Desktop\\SE\\Otsimo.accdb;'
        conn=pyodbc.connect(con_string)
        cursor=conn.cursor()
        myrecord=((user,game,score,curr_date,curr_time))
        cursor.execute('INSERT INTO PROGRESS VALUES (?,?,?,?,?)', myrecord)
        print("Data Inserted")
        cursor.commit()

    except pyodbc.Error as e:
        print("Error in Connection",e)

def con_login(u,p):
    try:
        con_string=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\92333\\Desktop\\SE\\Otsimo.accdb;'
        conn=pyodbc.connect(con_string)
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM LOGIN')
        for row in cursor.fetchall():
            username = row.User.strip()  # Assuming the column name for username is "username"
            password = row.Pass # Assuming the column name for password is "password"
            #print(f"Stored username: {username}, Stored password: {password}")
            #print(f"Entered username: {u}, Entered password: {p}")

            if username == u and password == p:
                return True
        
        return False

    except pyodbc.Error as e:
        print("Error in Connection",e) 
def con_fetch(username):
    try:
        con_string=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\92333\\Desktop\\SE\\Otsimo.accdb;'
        conn=pyodbc.connect(con_string)
        cursor=conn.cursor()
        cursor.execute('SELECT Game,Score,Date_ FROM PROGRESS WHERE USER=?',username)
        row=cursor.fetchall()
        return row

    except pyodbc.Error as e:
        print("Error in Connection",e) 
a=con_fetch('aafifa')
print(a)