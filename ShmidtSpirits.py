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
        new_table = "CREATE TABLE D" + d.strftime("%y%m%d") + " (ID INTEGER AUTO_INCREMENT PRIMARY KEY, Time VARCHAR(10), Supply_STPT INTEGER(8), Supply_Temp FLOAT(8), Deph_Ret_STPT INTEGER(8), Deph_Ret_Temp FLOAT(8))"
        self.C.execute(new_table)

    def addData(self, Supply_STPT, Supply_Temp, Deph_Ret_STPT, Deph_Ret_Temp):
        d = datetime.datetime.now()
        sql = "INSERT INTO D" + d.strftime("%y%m%d") + " (Time, Supply_STPT, Supply_Temp, Deph_Ret_STPT, Deph_Ret_Temp) VALUES (%s, %s, %s, %s, %s)"
        val = (d.strftime("%X"),Supply_STPT, Supply_Temp, Deph_Ret_STPT, Deph_Ret_Temp)
        self.C.execute(sql,val)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()


# ************************************************************************* #
#                                                                           #
#                                   Main Code                               #
#                                                                           #
# ************************************************************************* #
if __name__ == "__main__":

    data = database()
    data.connect()
    data.addTable()
    counter = 0
    for x in range(60):
        counter = x + randint(0,10)
        data.addData(90,counter+0.1,140,counter+50+0.1)
        print("X: {}, temp {}".format(x,counter))
        time.sleep(1)

    data.disconnect()
