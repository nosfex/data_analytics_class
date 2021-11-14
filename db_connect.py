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
    
    def close(self):
        self.cursor.close()
        self.conn.close()