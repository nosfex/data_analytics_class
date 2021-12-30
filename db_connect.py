import pymssql
from os import getenv

class DBConnect:

    def __init__(self):

        self.conn = pymssql.connect(
            host= r'coderhouse18890.database.windows.net',   
            user='coder_admin',
            password='etc_1234',
            database='imporfrut19_21'
        )
        self.cursor = self.conn.cursor()
    
    def insert_into_db(self, force_commit, query, client_list):
        self.cursor.execute(query, client_list)
        if force_commit == True:
            self.force_db_commit()
        

    def force_db_commit(self):
        self.conn.commit()


    #dupe function, need to manipulate data more to understand how every insert is going to differ
    def close(self):
        self.cursor.close()
        self.conn.close()