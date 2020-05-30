from random import randint
import mariadb
import datetime
import time

class database:
    def __init__(self):
        self.table = None
        self.conn = None
        self.C = None

    def connect(self):
        self.conn = mariadb.connect(
            user="root",
            password="password",
            host="localhost",
            database="distilling"
            )
        self.C = self.conn.cursor()

    def addTable(self):
        d = datetime.datetime.now()
        new_table = "CREATE TABLE D" + d.strftime("%y%m%d") + " (Time VARCHAR(10), Temp INTEGER(8), ID INTEGER AUTO_INCREMENT PRIMARY KEY)"
        self.C.execute(new_table)

    def addData(self,temperature):
        d = datetime.datetime.now()
        sql = "INSERT INTO D" + d.strftime("%y%m%d") + " (Time, Temp) VALUES (%s, %s)"
        val = (d.strftime("%X"),temperature)
        self.C.execute(sql,val)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()



if __name__ == "__main__":

    data = database()
    data.connect()
    data.addTable()
    counter = 0
    for x in range(60):
        counter = x + randint(0,10)
        data.addData(counter)
        print("X: {}, temp {}".format(x,counter))
        time.sleep(1)

    data.disconnect()
