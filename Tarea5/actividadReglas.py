from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from mongoDB import *

from pruebadatabasemysql import *


# Implementacion MySQL
dbMySQL = MySQL("sql10.freesqldatabase.com","sql10689405","ACM1wVFXPb","sql10689405")
reporte1 = Reporte(1,dbMySQL)

reporte1._baseDeDatos.insertar("Reporte","testIOnsert","2024-03-15")
reporte1._baseDeDatos.abrir("2024-03-15")
reporte1._baseDeDatos.actualizar("Reporte","Hola","2024-03-15")
reporte1._baseDeDatos.eliminar("Reporte","2024-03-15")
reporte1._baseDeDatos.abrir("2024-03-15")

dbMongoDB = MongoDB("mongodb+srv://admin:admin@cluster0.evbfjj7.mongodb.net/?retryWrites=true&w=majority&test/test=Cluster0","mi_base_de_datos","mi_coleccion")

reporte2 = Reporte(2,dbMongoDB)
reporte2._baseDeDatos.insertar(2,"Hola mundo","2024-03-14")
reporte2._baseDeDatos.abrir(2)
reporte2._baseDeDatos.actualizar("Hola mundo","2024-03-15")
reporte2._baseDeDatos.eliminar(1)

