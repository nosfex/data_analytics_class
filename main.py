from csv_helper import CSVHelper, Client, ClientParser 
from csv_helper import ClientParser 
from db_connect import DBConnect
helper = CSVHelper()
helper.open('csv_export.csv')
clients = ClientParser()
#clients.process_client_list(helper)
#clients.process_operation(helper)
clients.process_vendor(helper)
db = DBConnect()
#for x in range(len(clients.ids)):
	#db.insert_client("INSERT INTO dbo.CLIENTE VALUES (%s, %s, %s, %s, %s, %s)", (clients.ids[x], clients.names[x], 0, 0, 0, 0))
#for x in clients.operation:
	#db.insert_client('INSERT INTO dbo.entregas VALUES (%s, %s, %s, %s, %s)', (x['Folio'], x['Tipo'], x['Fecha'], x['Producto'], x['Cantidad']))
inc = 0
for x in clients.vendor:
	inc = inc + 1
	db.insert_client('INSERT INTO dbo.VENDEDOR VALUES (%s, %s, %s)', (inc , x['Vendedor'], x['Plaza']))
db.close()