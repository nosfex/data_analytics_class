import pymssql
from os import getenv

class DBConnect:

    def __init__(self):

        self.conn = pymssql.connect(
            host= r'DESKTOP-US1BF8U\SQLEXPRESS',    
            database='imporfrut19_21'
        )
        self.cursor = self.conn.cursor()
    
    def insert_client(self, query, client_list):
        self.cursor.execute(query, client_list)
        self.conn.commit()

    #dupe function, need to manipulate data more to understand how every insert is going to differ
    def insert_operation(self, query, operation_data):
        self.cursor.execute(query, operation_data )
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()