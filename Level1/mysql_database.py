import mysql.connector
class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection = mysql.connector.connect(host=self.host,database=self.db,user=self.user,password=self.password)
        except:
            print("Error while connecting to the database")

    def inser_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s);" #passing variables/parameters so that we using %s
        val=(self.filename)

        self.cur.execute(sql,(val,))

        self.connection.commit()
    def search(self):
        self.cur = self.connection.cursor()
        sql = "SELECT *FROM files limit 0,10"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
dbobj=Mysql_DBaccess('Localhost', 'root', 'Jyo@#$767207', 'searchfiles')
dbobj.inser_data('c://HCL1/Sql file 1.txt')
print(dbobj)
