from pymongo import MongoClient
from pymongo.server_api import ServerApi

from database import *

uri1 = "mongodb+srv://admin:admin@cluster0.evbfjj7.mongodb.net/?retryWrites=true&w=majority&test/test=Cluster0"
database_name1 = "mi_base_de_datos"
collection_name1 = "mi_coleccion"


#Clase de MongoDB  
class MongoDB(DataBase):
    def __init__(self, uri, data_base_name, collection_name):
        self._uri = uri
        self._data_base_name = data_base_name
        self._collection_name = collection_name

    def conection(self):
        uri = self._uri
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Specify the database and collection
        database_name = self._data_base_name
        collection_name = self._collection_name
        db = client[database_name]
        return db[collection_name]
        
    def insertar(self,id,  data: str, date: str) -> bool:
        collection = self.conection()
        # Data to be inserted
        data_to_insert = {
            "id" : id,
            "data": data,
            "date": date
        }

        # Insert one document
        result = collection.insert_one(data_to_insert)

        # Print the inserted document's ID
        print("Document inserted with ID:", result.inserted_id)

    
    def actualizar(self, data: str, date: str) -> bool:
        collection = self.conection()
        self.data = data
        data_to_update = {
            "date": date,
        }

        # Corrección en la llamada a update_one
        result = collection.update_one({"data": data}, {"$set": {"date": date}})

        print("Document updated with ID")

 
    
    def eliminar(self, data: str) -> bool:
        collection = self.conection()
        result = collection.delete_one({"id":1})
        print("The file was deleted")

    def abrir(self, id: int):
        collection = self.conection()
        results = collection.find_one({"id":id})
        print (results)

mongotest = MongoDB(uri1,database_name1,collection_name1)
#mongotest.insertar(1,"Test2","2024-03-15")
mongotest.eliminar(1)