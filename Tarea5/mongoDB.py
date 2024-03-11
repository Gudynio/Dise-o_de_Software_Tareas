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
        
    def insertar(self, data: str, date: str) -> bool:
        collection = self.conection()
        # Data to be inserted
        data_to_insert = {
            "data": "test",
            "date": "2024-03-12"
        }

        # Insert one document
        result = collection.insert_one(data_to_insert)

        # Print the inserted document's ID
        print("Document inserted with ID:", result.inserted_id)

    
    def actualizar(self, data: str) -> bool:
        return super().actualizar(data)
    
    def eliminar(self, data: str) -> bool:   
        return super().eliminar(data)

mongotest = MongoDB(uri1,database_name1,collection_name1)
mongotest.insertar("Test2","2024-03-14")