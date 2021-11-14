from csv_helper import CSVHelper, Client, ClientParser 
from csv_helper import ClientParser 
from db_connect import DBConnect
helper = CSVHelper()
helper.open('csv_export.csv')
clients = ClientParser()
clients.process_client_list(helper)

db = DBConnect()
print([clients.clients[0].id, clients.clients[0].name])
for x in range(len(clients.ids)):
	db.insert_client("INSERT INTO dbo.CLIENTE VALUES (%s, %s, %s, %s, %s, %s)", (clients.ids[x], clients.names[x], 0, 0, 0, 0))
db.close()