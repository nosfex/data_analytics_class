import csv
class CSVHelper:
    def __init__(self):
        self.reader = ''
    def open(self, filename):
        csvfile = open(filename, newline='', encoding='utf8') 
        self.reader = csv.DictReader(csvfile)
    
class ClientParser:
    
    def __init__(self):
        self.clients = []
        self.names = []
        self.ids = []
        self.operation = []
        self.vendor = []

    def process_client_list(self, csvhelper):
        for row in csvhelper.reader:
            cl = Client(row['IDAuxiliar'], row['Auxiliar'])
            if len(self.clients) <= 0:
                self.clients.append(cl)
                self.ids.append(row['IDAuxiliar'])
                self.names.append(row['Auxiliar'])
            else:
                unique = True
                for client in self.clients:
                    if client.id == cl.id:
                        unique = False
                if unique == True:
                    self.clients.append(cl)
                    self.ids.append(row['IDAuxiliar'])
                    self.names.append(row['Auxiliar'])
      
    def process_operation(self, csvhelper):
        self.seen = set()
        for row in csvhelper.reader:
            op = {'Folio':row['Folio'], 'Tipo':row['IDTipoDocumento'], 'Fecha':'10-10-2020', 'Producto':row['Producto'], 'Cantidad':row['Cantidad']}
            if len(self.operation) <= 0:
                self.operation.append(op)
                self.seen.add(row['Folio'])
           
            else:
                val = row['Folio'] in self.seen
                if val == False:
                    self.operation.append(op)
                    self.seen.add(row['Folio'])

    def process_vendor(self, csvhelper):
        self.seen = set()
        for row in csvhelper.reader:
            op = {'Vendedor':row['Vendedor'], 'Plaza':row['ReferenciaAdic1']}
            if len(self.vendor) <= 0:
                self.vendor.append(op)
                self.seen.add(row['Vendedor'])
           
            else:
                val = row['Vendedor'] in self.seen
                if val == False:
                    self.vendor.append(op)
                    self.seen.add(row['Vendedor'])



class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name