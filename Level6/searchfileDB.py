import mysql.connector
class searchFilesDB:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection = mysql.connector.connect(host=self.host,database=self.db,user=self.user,password=self.password)
        except:
            print("Error while connecting to the database")



    def searchDB(self, fil):
        self.f = "filename"
        # data=(filename)
        self.cur = self.connection.cursor()
        sql = """select * from files where filename like'%{0}'""".format(fil)
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row == None:
            return 0
        else:
            return row




dbobj=searchFilesDB('localhost', 'root', 'Jyo@#$767207', 'searchfiles')
#obj=inser_data('C://HCL1//Sql file 1.txt')
print(dbobj.searchDB('c://HCL1/Sql file 1.txt'))

