from csv_helper import CSVHelper, Client, ClientParser 
from csv_helper import ClientParser 
from db_connect import DBConnect
helper = CSVHelper()
helper.open('csv_export_0_1.csv')
clients = ClientParser()
#clients.process_client_list(helper)
clients.process_operation(helper)
#clients.process_product(helper)
#clients.process_vendor(helper)
db = DBConnect()
for x in clients.clients:
	db.insert_into_db(False, "INSERT INTO dbo.CLIENTE VALUES (%s, %s, %s, %s, %s, %s)", (x['ID'], x['Nombre'], 0, 0, 0, 0))
inc = 0

for x in clients.vendor:
	inc = inc + 1
	db.insert_into_db(False, 'INSERT INTO dbo.VENDEDOR VALUES (%s, %s, %s)', (inc, x['Vendedor'], x['Plaza']))
for x in clients.product:	#inc = inc + 1
	db.insert_into_db(False, 'INSERT INTO dbo.PRODUCTO VALUES (%s, %s)', (x['IDProducto'], x['NombreProducto']))

for x in clients.operation:	
	db.insert_into_db(False,'INSERT INTO dbo.ENTREGAS VALUES (%s, %s, %s, %s, %s, %s, %s)', (x['Folio'], x['Tipo'], x['Vendedor'], x['IDCliente'], x['Fecha'], x['Producto'], x['Cantidad']))

db.force_db_commit()
db.close()