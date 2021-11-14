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
           


class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name